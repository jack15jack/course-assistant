from datetime import datetime
from pydantic import BaseModel


class JobResponse(BaseModel):

    id: int
    document_id: int
    job_type: str
    status: str
    progress: int
    error_message: str | None
    created_at: datetime
    updated_at: datetime


    class Config:
        from_attributes = True