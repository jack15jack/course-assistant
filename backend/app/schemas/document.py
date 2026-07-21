from datetime import datetime
from pydantic import BaseModel, ConfigDict
from .job import JobResponse


class DocumentResponse(BaseModel):
    id: int
    course_id: int
    filename: str
    filepath: str
    file_type: str
    status: str
    created_at: datetime

    jobs: list[JobResponse] = []

    model_config = ConfigDict(from_attributes=True)