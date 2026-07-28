from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import Base


class Course(Base):

    __tablename__ = "courses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    semester = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    documents = relationship(
    "Document",
    back_populates="course",
    cascade="all, delete-orphan"
    )

