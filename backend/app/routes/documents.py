from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import (
    save_document,
    get_documents,
    get_document_by_id,
    delete_document
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/{course_id}", response_model=DocumentResponse)
def upload_document(
    course_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return save_document(db, course_id,file)


@router.get("/", response_model=list[DocumentResponse])
def get_all_documents(
    db: Session = Depends(get_db)
):
    return get_documents(db)


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    return get_document_by_id(db, document_id)


@router.delete("/{document_id}")
def delete_document_endpoint(
    document_id: int,
    db: Session = Depends(get_db)
):
    return delete_document(db, document_id)