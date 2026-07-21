from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.course import Course
from app.models.document import Document
from app.schemas.course import CourseCreate


def get_courses(db: Session):

    return db.query(Course).all()


def get_course_by_id(db, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course


def create_course(
    db: Session,
    course: CourseCreate
):

    new_course = Course(
        name=course.name,
        semester=course.semester,
        description=course.description
    )

    db.add(new_course)

    db.commit()

    db.refresh(new_course)

    return new_course


def update_course(db, course_id: int, course_data):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    course.name = course_data.name
    course.semester = course_data.semester
    course.description = course_data.description

    db.commit()
    db.refresh(course)

    return course


def delete_course(db, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    db.delete(course)
    db.commit()

    return {"message": "Course deleted successfully"}


def get_course_documents(db, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return (
        db.query(Document)
        .filter(Document.course_id == course_id)
        .all()
    )