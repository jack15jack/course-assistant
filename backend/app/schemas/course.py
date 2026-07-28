from pydantic import BaseModel
from app.schemas.document import DocumentResponse


class CourseCreate(BaseModel):

    name: str
    semester: str
    description: str | None = None


class CourseResponse(BaseModel):

    id: int
    name: str
    semester: str
    description: str | None
    documents: list[DocumentResponse] = []

    class Config:
        from_attributes = True