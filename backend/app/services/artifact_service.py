from sqlalchemy.orm import Session
from pathlib import Path

from app.models.artifact import Artifact
from app.models.document import Document
from app.models.course import Course

from ai.artifact_generators.notes import NotesGenerator
from ai.artifact_generators.study_guides import StudyGuideGenerator
from ai.artifact_generators.formulas import FormulaGenerator
from ai.artifact_generators.exams import ExamGenerator
from app.utils.pdf_utils import markdown_to_pdf
from app.utils.file_utils import get_course_generated_directory

GENERATORS = {
    "notes": NotesGenerator,
    "studyguide": StudyGuideGenerator,
    "formula": FormulaGenerator,
    "exam": ExamGenerator,
}

SCOPES = {"course", "document"}

def create_artifact(
    db: Session,
    scope_id: int,
    scope: str,
    artifact_type: str,
    title: str,
    filepath: str
):

    artifact = Artifact(
        scope=scope,
        scope_id=scope_id,
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
    scope_id: int,
    artifact_type: str,
    scope: str
):

    if artifact_type not in GENERATORS:
        raise Exception(f"Unsupported artifact type: {artifact_type}")

    if scope not in SCOPES:
        raise Exception(f"Unsupported scope: {scope}")


    # Resolve course directory
    if scope == "document":
        document = (db.query(Document).filter(Document.id == scope_id).first())

        if document is None:
            raise Exception("Document not found")

        course = (db.query(Course).filter(Course.id == document.course_id).first())

        if course is None:
            raise Exception("Course not found")

        prefix = f"document_{scope_id}"

    else:
        course = (db.query(Course).filter(Course.id == scope_id).first())

        if course is None:
            raise Exception("Course not found")

        prefix = f"course_{scope_id}"

    output_dir = get_course_generated_directory(course.id, course.name)

    output_dir.mkdir(parents=True, exist_ok=True )

    # Generate artifact
    generator = GENERATORS[artifact_type](db=db)
    markdown = generator.generate(scope, scope_id)

    # Temporary markdown file
    md_path = output_dir / f"{prefix}_{artifact_type}.md"
    md_path.write_text(markdown, encoding="utf-8")

    # PDF output
    pdf_path = output_dir / f"{prefix}_{artifact_type}.pdf"
    markdown_to_pdf(markdown_path=str(md_path), pdf_path=str(pdf_path))

    # Remove temporary markdown
    md_path.unlink(missing_ok=True)

    return create_artifact(
        db=db,
        scope=scope,
        scope_id=scope_id,
        artifact_type=artifact_type,
        title=f"{artifact_type.replace('_', ' ').title()} - {scope.title()} {scope_id}",
        filepath=str(pdf_path)
    )


def get_artifact(
    db: Session,
    artifact_id: int
):
    artifact = (db.query(Artifact).filter(Artifact.id == artifact_id).first())

    if artifact is None:
        raise Exception("Artifact not found")

    return artifact


def get_document_artifacts(
    db: Session,
    document_id: int
):

    return (
        db.query(Artifact).filter(Artifact.scope == "document", Artifact.scope_id == document_id).order_by(Artifact.created_at.desc()).all())


def get_course_artifacts(
    db: Session,
    course_id: int
):
    artifacts = (
        db.query(Artifact)
        .filter(Artifact.scope == "course", Artifact.scope_id == course_id)
        .order_by(Artifact.created_at.desc())
        .all()
    )

    document_artifacts = (
        db.query(Artifact)
        .join(Document, Artifact.scope_id == Document.id)
        .filter(Artifact.scope == "document", Document.course_id == course_id)
        .order_by(Artifact.created_at.desc())
        .all()
    )

    return artifacts + document_artifacts


def delete_artifact(
    db: Session,
    artifact_id: int
):

    artifact = get_artifact(db, artifact_id)

    pdf = Path(artifact.filepath)

    if pdf.exists():
        pdf.unlink()

    db.delete(artifact)
    db.commit()

    return {"success": True}