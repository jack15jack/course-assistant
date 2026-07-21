from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.course import CourseCreate
from app.services.course_service import (
    create_course,
    get_courses,
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


@router.post("/")
def create_new_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    return create_course(db, course)