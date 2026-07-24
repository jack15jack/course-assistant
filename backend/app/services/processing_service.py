from sqlalchemy.orm import Session

from datetime import datetime

from app.models.job import Job
from app.models.document import Document
from app.services.content_service import add_document_content
from app.services.section_service import add_section
from ai.ingestion.router import extract_document
from ai.processing.normalize import normalize_text
from ai.processing.sectioning import detect_sections



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
    
    job = (db.query(Job).filter(Job.document_id == document_id,Job.job_type == "document_processing").order_by(Job.id.desc()).first())

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
        contents = extract_document(document.filepath, document.file_type)

        for item in contents:

            normalized = normalize_text(item["content"])

            item["content"] = normalized

            add_document_content(
                db=db,
                document_id=document.id,
                content=item["content"],
                content_type=item["content_type"],
                metadata=item["metadata"]
            )

            sections = detect_sections(normalized)

            for section in sections:
                add_section(
                    db=db,
                    document_id=document.id,
                    section_data=section
                )
            
        db.commit()

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