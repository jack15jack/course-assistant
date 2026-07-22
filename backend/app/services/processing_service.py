from sqlalchemy.orm import Session

from datetime import datetime

from app.models.job import Job
from app.models.document import Document
from ai.ingestion.router import extract_document
from app.services.content_service import add_document_content


def create_processing_job(
    db: Session,
    document_id: int,
    job_type: str
):

    job = Job(
        document_id=document_id,
        job_type=job_type,
        status="queued",
        progress=0
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def process_document(
    db: Session,
    document_id: int
):
    
    job = (db.query(Job).filter(document_id, "document_processing").order_by(Job.id.desc()).first())

    if not job:
        raise Exception("Processing job not found")
    

    try:
        # mark job running
        job.status = "running"
        job.progress = 10
        job.updated_at = datetime.utcnow()

        db.commit()

        document = (db.query(Document).filter(Document.id == document_id).first())

        if not document:
            raise Exception("Document not found")
        
        #extraction
        contents = extract_document(document.filepath)

        job.progress = 50
        job.updated_at = datetime.utcnow()

        db.commit()

        for item in contents:
            add_document_content(
                db=db,
                document_id=document.id,
                content=item["content"],
                content_type=item["content_type"],
                metadata=item["metadata"]
            )

        # complete
        job.status = "completed"
        job.progress = 100
        job.updated_at = datetime.utcnow()

        document.status = "processed"

        db.commit()

        return job

    except Exception as e:
        job.status = "failed"
        job.error_message = str(e)
        job.updated_at = datetime.utcnow()

        db.commit()

        raise e