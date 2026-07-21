from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.job import Job
from app.schemas.job import JobResponse
from app.services.processing_service import process_document


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/{job_id}", response_model=JobResponse)
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    return (db.query(Job).filter(Job.id == job_id).first())


@router.post("/documents/{document_id}")
def process_document_job(
    document_id: int,
    db: Session = Depends(get_db)
):

    return process_document(
        db,
        document_id
    )