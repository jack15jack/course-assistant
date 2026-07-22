from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    ForeignKey,
    DateTime,
    JSON
)

from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class DocumentContent(Base):

    __tablename__ = "document_contents"

    id = Column(Integer, primary_key=True)

    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)

    content_type = Column(String, nullable=False)

    content = Column(Text, nullable=False)

    content_metadata = Column("metadata", JSON, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    document = relationship("Document", back_populates="contents")