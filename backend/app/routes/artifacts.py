from pathlib import Path
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.artifact import ArtifactResponse

from app.services.artifact_service import (
    generate_artifact, 
    get_artifact,
    get_document_artifacts,
    get_course_artifacts,
    delete_artifact
)


router = APIRouter(prefix="/artifacts", tags=["artifacts"])

@router.post("/gen/{scope}/{scope_id}/{artifact_type}", response_model=ArtifactResponse)
def create_document_artifact(
    scope_id: int,
    scope: str,
    artifact_type: str,
    db: Session = Depends(get_db)
):
    return generate_artifact(
        db=db,   
        scope=scope,    
        scope_id=scope_id,
        artifact_type=artifact_type
    )


@router.get("/{artifact_id}")
def read_artifact(
    artifact_id: int,
    db: Session = Depends(get_db)
):
    return get_artifact(db, artifact_id)


@router.get("/document/{document_id}")
def read_document_artifacts(
    document_id: int,
    db: Session = Depends(get_db)
):
    return get_document_artifacts(db, document_id)


@router.get("/course/{course_id}")
def read_course_artifacts(
    course_id: int,
    db: Session = Depends(get_db)
):
    return get_course_artifacts(db, course_id)


@router.get("/{artifact_id}/download")
def download_artifact(
    artifact_id: int,
    db: Session = Depends(get_db)
):

    artifact = get_artifact(db, artifact_id)

    return FileResponse(
        artifact.filepath,
        media_type="application/pdf",
        filename=Path(artifact.filepath).name
    )


@router.delete("/{artifact_id}")
def delete_artifact_endpoint(
    artifact_id: int,
    db: Session = Depends(get_db)
):
    return delete_artifact(db, artifact_id)