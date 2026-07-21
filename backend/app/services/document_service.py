import os
from sqlalchemy.orm import Session
from app.models.document import Document

UPLOAD_DIR = "uploads"

def save_document(
    db: Session,
    course_id: int,
    filename: str,
    filepath: str,
    file_type: str
):

    document = Document(
        course_id=course_id,
        filename=filename,
        filepath=filepath,
        file_type=file_type
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document