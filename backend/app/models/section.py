from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Section(Base):

    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False
    )

    # Example:
    # "Chapter 3: Fourier Transform"
    # "3.2 Properties of the Fourier Transform"
    title = Column(
        String,
        nullable=False
    )

    # Heading depth
    #
    # 1 = Chapter
    # 2 = Subsection
    # 3 = Sub-subsection
    level = Column(
        Integer,
        nullable=False,
        default=1
    )

    # Text belonging to this section
    content = Column(
        Text,
        nullable=False
    )

    # Ordering inside the document
    # Example:
    # Section 1
    # Section 2
    # Section 3
    position = Column(
        Integer,
        nullable=False,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    document = relationship(
        "Document",
        back_populates="sections"
    )

    chunks = relationship(
        "Chunk",
        back_populates="section",
        cascade="all, delete-orphan"
    )