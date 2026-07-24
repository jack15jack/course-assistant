from pydantic import BaseModel
from datetime import datetime


class ArtifactCreate(BaseModel):
    document_id: int
    artifact_type: str


class ArtifactResponse(BaseModel):
    id: int
    document_id: int
    artifact_type: str
    title: str
    filepath: str
    created_at: datetime

    class Config:
        from_attributes = True