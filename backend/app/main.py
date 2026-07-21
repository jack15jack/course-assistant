from fastapi import FastAPI

from app.routes.courses import router as courses_router


app = FastAPI(
    title="Study Assistant API",
    version="0.1.0"
)

app.include_router(courses_router)


@app.get("/")
def root():

    return {
        "message": "Study Assistant API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }