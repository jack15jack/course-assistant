from sqlalchemy.orm import Session

from app.models.document_content import DocumentContent


def add_document_content(
    db: Session,
    document_id: int,
    content_type: str,
    content: str,
    metadata: dict | None = None
):

    content_entry = DocumentContent(
        document_id=document_id,
        content_type=content_type,
        content=content,
        metadata=metadata
    )

    db.add(content_entry)
    db.commit()
    db.refresh(content_entry)

    return content_entry