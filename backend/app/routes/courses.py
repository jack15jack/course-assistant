from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.course import (CourseCreate, CourseResponse)
from app.schemas.document import DocumentResponse
from app.services.course_service import (
    create_course,
    get_courses,
    get_course_by_id,
    update_course,
    delete_course,
    get_course_documents
)


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get("/")
def list_courses(
    db: Session = Depends(get_db)
):

    return get_courses(db)


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return get_course_by_id(db, course_id)


@router.post("/")
def create_new_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    return create_course(db, course)

@router.put("/{course_id}", response_model=CourseResponse)
def update_existing_course(
    course_id: int,
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return update_course(db, course_id, course)


@router.delete("/{course_id}")
def delete_existing_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return delete_course(db, course_id)


@router.get("/{course_id}/documents", response_model=list[DocumentResponse])
def get_documents_for_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return get_course_documents(db, course_id)