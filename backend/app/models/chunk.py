from sqlalchemy import Column, Integer, Text, ForeignKey, JSON, Float, ARRAY
from sqlalchemy.orm import relationship

from app.database import Base


class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=False
    )

    section_id = Column(
        Integer,
        ForeignKey("sections.id"),
        nullable=True
    )

    content = Column(
        Text,
        nullable=False
    )

    chunk_index = Column(
        Integer,
        nullable=False
    )

    chuck_metadata = Column(
        "metadata",
        JSON,
        nullable=True
    )

    embedding = Column(
        ARRAY(Float),
        nullable=True
    )

    document = relationship(
        "Document",
        back_populates="chunks"
    )

    section = relationship(
        "Section",
        back_populates="chunks"
    )