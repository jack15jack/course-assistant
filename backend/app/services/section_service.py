from sqlalchemy.orm import Session

from app.models.section import Section


def create_section(
    db: Session,
    document_id: int,
    title: str,
    level: int,
    content: str
):

    section = Section(
        document_id=document_id,
        title=title,
        level=level,
        content=content
    )

    db.add(section)
    db.commit()
    db.refresh(section)

    return section