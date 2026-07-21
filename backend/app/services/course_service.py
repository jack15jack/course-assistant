from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course import CourseCreate


def get_courses(db: Session):

    return db.query(Course).all()


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