import os
import shutil
from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.document_service import save_document


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_DIR = "uploads"

@router.post("/{course_id}")
def upload_document(
    course_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(filepath, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    document = save_document(
        db=db,
        course_id=course_id,
        filename=file.filename,
        filepath=filepath,
        file_type=file.content_type
    )

    return document