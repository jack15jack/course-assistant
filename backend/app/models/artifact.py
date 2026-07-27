from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Artifact(Base):

    __tablename__ = "artifacts"


    id = Column(Integer, primary_key=True, index=True)

    scope = Column(String, nullable=False)

    scope_id = Column(Integer, nullable=False)  

    artifact_type = Column(String, nullable=False)

    title = Column(String, nullable=False)

    filepath = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)