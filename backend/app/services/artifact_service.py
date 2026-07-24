from sqlalchemy.orm import Session
from pathlib import Path

from app.models.artifact import Artifact

from app.services.artifact_service import create_artifact

from ai.artifact_generators.notes import NotesGenerator
from ai.artifact_generators.study_guides import StudyGuideGenerator
from ai.artifact_generators.formulas import FormulaGenerator
from ai.artifact_generators.exams import ExamGenerator

GENERATED_DIR = Path("generated")

GENERATORS = {
    "notes": NotesGenerator,
    "studyguide": StudyGuideGenerator,
    "formula": FormulaGenerator,
    "exam": ExamGenerator,
}

def create_artifact(
    db: Session,
    document_id: int,
    artifact_type: str,
    title: str,
    filepath: str
):

    artifact = Artifact(
        document_id=document_id,
        artifact_type=artifact_type,
        title=title,
        filepath=filepath
    )


    db.add(artifact)
    db.commit()
    db.refresh(artifact)

    return artifact


def generate_artifact(
    db: Session,
    document_id: int,
    artifact_type: str
):

    if artifact_type not in GENERATORS:
        raise Exception(f"Unsupported artifact type: {artifact_type}")

    GENERATED_DIR.mkdir(exist_ok=True)

    # Instantiate generator
    generator_class = GENERATORS[artifact_type]
    generator = generator_class()

    markdown = generator.generate(document_id)

    # Save markdown
    filename = (f"document_{document_id}_{artifact_type}.md")
    filepath = GENERATED_DIR / filename
    filepath.write_text(markdown, encoding="utf-8")

    # Store metadata
    artifact = create_artifact(
        db=db,
        document_id=document_id,
        artifact_type=artifact_type,
        title=f"{artifact_type.replace('_', ' ').title()} - Document {document_id}",
        filepath=str(filepath)
    )

    return artifact
