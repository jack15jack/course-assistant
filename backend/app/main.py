from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.courses import router as courses_router
from app.routes.documents import router as documents_router
from app.routes.jobs import router as jobs_router
from app.routes.artifacts import router as artifacts_router


app = FastAPI(
    title="Study Assistant API",
    version="0.1.0"
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(courses_router)
app.include_router(documents_router)
app.include_router(jobs_router)
app.include_router(artifacts_router)


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