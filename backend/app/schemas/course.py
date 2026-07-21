from pydantic import BaseModel


class CourseCreate(BaseModel):

    name: str
    semester: str
    description: str | None = None


class CourseResponse(BaseModel):

    id: int
    name: str
    semester: str
    description: str | None

    class Config:
        from_attributes = True