from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False
    )

    # Example:
    # "pdf_extract"
    # "generate_notes"
    # "create_flashcards"
    job_type = Column(
        String,
        nullable=False
    )

    # queued, running, completed, failed
    status = Column(
        String,
        default="queued",
        nullable=False
    )

    progress = Column(
        Integer,
        default=0
    )

    error_message = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    document = relationship(
        "Document",
        back_populates="jobs"
    )