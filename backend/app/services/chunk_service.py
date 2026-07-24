from sqlalchemy.orm import Session
from app.models.chunk import Chunk


def add_chunk(
    db: Session,
    document_id: int,
    section_id: int | None,
    content: str,
    chunk_index: int,
    metadata: dict | None = None,
    embedding: list[float] | None = None,
):

    chunk = Chunk(
        document_id=document_id,
        section_id=section_id,
        content=content,
        chunk_index=chunk_index,
        metadata=metadata,
        embedding=embedding,
    )

    db.add(chunk)

    return chunk