from sqlalchemy.orm import Session

from app.models.job import Job
from app.models.document import Document
from ai.ingestion.pdf import extract_pdf_text


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
    
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not document:
        raise Exception("Document not found")

    document.status = "processing"

    db.commit()

    try:
        if document.file_type == "application/pdf":
            text = extract_pdf_text(document.filepath)

        else:
            raise Exception("Unsupported file type")

        document.extracted_text = text
        document.status = "processed"

        db.commit()
        db.refresh(document)

        return document

    except Exception as e:
        document.status = "failed"
        db.commit()
        raise e