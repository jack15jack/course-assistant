from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.artifact import ArtifactResponse

from app.services.artifact_service import generate_artifact


router = APIRouter(
    prefix="/artifacts",
    tags=["artifacts"]
)

@router.post(
    "/documents/{document_id}/{artifact_type}",
    response_model=ArtifactResponse
)
def create_document_artifact(
    document_id: int,
    artifact_type: str,
    db: Session = Depends(get_db)
):

    return generate_artifact(
        db=db,
        document_id=document_id,
        artifact_type=artifact_type
    )