from sqlalchemy.orm import Session

from app.models.section import Section



def add_section(
    db: Session,
    document_id: int,
    section_data: dict
):

    section = Section(
        document_id=document_id,
        title=section_data["title"],
        content=section_data["content"],
        level=section_data["level"],
        position=section_data["position"]
    )

    db.add(section)

    return section