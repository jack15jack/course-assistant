from pathlib import Path
import shutil
import uuid
from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.models.course import Course
from app.models.document import Document
from app.utils.file_utils import get_course_upload_directory
from app.services.processing_service import create_processing_job

def save_document(
    db: Session,
    course_id: int,
    file: UploadFile
):
    
    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    upload_dir = get_course_upload_directory(
        course.id,
        course.name
    )

    upload_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    extension = Path(file.filename).suffix

    stored_filename = (f"{uuid.uuid4()}{extension}")

    destination = upload_dir / stored_filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    document = Document(
        course_id=course_id,
        filename=file.filename,
        filepath=str(destination),
        file_type=file.content_type
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    job = create_processing_job(
        db=db,
        document_id=document.id,
        job_type="document_processing"
    )

    return document

def get_documents(db):
    return db.query(Document).all()


def get_document_by_id(db, document_id: int):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return document


def delete_document(db, document_id: int):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    db.delete(document)
    db.commit()

    path = Path(document.filepath)

    if path.exists():
        path.unlink()

    return {"message": "Document deleted successfully"}