from sqlalchemy.orm import Session

from app.models.course import Course
from app.models.document import Document
from app.models.section import Section
from app.models.chunk import Chunk


class ContextBuilder:

    def __init__(self, db: Session):
        self.db = db


    # Documents

    def build_document_context(self, document_id: int) -> dict:

        document = (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if not document:
            raise Exception("Document not found")

        return {
            "document": {
                "id": document.id,
                "filename": document.filename,
                "file_type": document.file_type,
            },
            "sections": self._load_sections(document.id)
        }

    def build_document_text(self, document_id: int):

        context = self.build_document_context(document_id)

        return self._context_to_text(context)


    # Courses

    def build_course_context(self, course_id: int):

        course = (
            self.db.query(Course)
            .filter(Course.id == course_id)
            .first()
        )

        if not course:
            raise Exception("Course not found")

        documents = (
            self.db.query(Document)
            .filter(Document.course_id == course_id)
            .filter(Document.status == "processed")
            .order_by(Document.id)
            .all()
        )

        return {
            "course": {
                "id": course.id,
                "name": course.name,
            },
            "documents": [
                self.build_document_context(doc.id)
                for doc in documents
            ]
        }

    def build_course_text(self, course_id):

        context = self.build_course_context(course_id)

        text = []

        for document in context["documents"]:

            text.append(
                f"# {document['document']['filename']}"
            )

            text.append(
                self._context_to_text(document)
            )

            text.append("")

        return "\n".join(text)

    
    # Sections

    def build_section_context(self, section_id):

        section = (
            self.db.query(Section)
            .filter(Section.id == section_id)
            .first()
        )

        if not section:
            raise Exception("Section not found")

        chunks = self._load_chunks(section.id)

        return {
            "id": section.id,
            "title": section.title,
            "level": section.level,
            "chunks": chunks,
        }

    def build_section_text(self, section_id):

        section = self.build_section_context(section_id)

        text = [f"# {section['title']}"]

        for chunk in section["chunks"]:
            text.append(chunk["content"])

        return "\n".join(text)

    
    # Arbitrary chunks

    def build_chunk_context(self, chunk_ids):

        chunks = (
            self.db.query(Chunk)
            .filter(Chunk.id.in_(chunk_ids))
            .order_by(Chunk.chunk_index)
            .all()
        )

        return [
            {
                "id": chunk.id,
                "content": chunk.content,
                "metadata": chunk.chunk_metadata,
            }
            for chunk in chunks
        ]

    def build_chunk_text(self, chunk_ids):

        chunks = self.build_chunk_context(chunk_ids)

        return "\n\n".join(
            chunk["content"]
            for chunk in chunks
        )


    # Prompt Builders

    # Full document - used in notes
    def build_full_context(
        self,
        document_id,
        max_characters=25000
    ):

        context = self.build_document_context(document_id)

        text = []

        current_size = 0

        for section in context["sections"]:

            header = f"# {section['title']}\n"

            if current_size + len(header) > max_characters:
                break

            text.append(header)

            current_size += len(header)

            for chunk in section["chunks"]:

                chunk_text = chunk["content"] + "\n\n"

                if current_size + len(chunk_text) > max_characters:
                    return "".join(text)

                text.append(chunk_text)

                current_size += len(chunk_text)

        return "".join(text)

    # Condensed - used in study guide
    def build_concise_context(
        self,
        document_id: int,
        max_characters: int = 12000
    ):

        context = self.build_document_context(document_id)

        text = []
        current_size = 0

        for section in context["sections"]:

            section_text = []

            section_text.append(f"# {section['title']}")

            # take the first 1-2 chunks as the section summary
            for chunk in section["chunks"][:2]:
                section_text.append(chunk["content"])

            section_block = "\n".join(section_text) + "\n\n"

            if current_size + len(section_block) > max_characters:
                break

            text.append(section_block)
            current_size += len(section_block)

        return "".join(text)

    # Only formula heavy chunks - used in formula sheet
    def build_formula_context(
        self,
        document_id: int,
        max_characters: int = 10000
    ):

        context = self.build_document_context(document_id)

        formula_keywords = [
            "=", "integral", "derivative", "sum", "sigma",
            "theta", "alpha", "beta", "lambda", "mu",
            "ohm", "volt", "amp", "watt", "newton",
            "joule", "pascal", "hertz"
        ]

        text = []
        current_size = 0

        for section in context["sections"]:

            section_added = False

            for chunk in section["chunks"]:

                content = chunk["content"]
                lower = content.lower()

                if any(k in lower for k in formula_keywords):

                    if not section_added:
                        header = f"# {section['title']}\n"
                        text.append(header)
                        current_size += len(header)
                        section_added = True

                    block = content + "\n\n"

                    if current_size + len(block) > max_characters:
                        return "".join(text)

                    text.append(block)
                    current_size += len(block)

        return "".join(text)

    # Concepts, formulas, and definitions - used in exams
    def build_exam_context(
        self,
        document_id: int,
        max_characters: int = 16000
    ):

        context = self.build_document_context(document_id)

        text = []
        current_size = 0

        for section in context["sections"]:

            section_text = []

            section_text.append(f"# {section['title']}")

            # include a small sample from the section
            for chunk in section["chunks"][:3]:
                section_text.append(chunk["content"])

            section_block = "\n".join(section_text) + "\n\n"

            if current_size + len(section_block) > max_characters:
                break

            text.append(section_block)
            current_size += len(section_block)

        return "".join(text)

    # Private Helpers

    def _load_sections(self, document_id):

        sections = (
            self.db.query(Section)
            .filter(Section.document_id == document_id)
            .order_by(Section.order_index)
            .all()
        )

        results = []

        for section in sections:

            results.append({
                "id": section.id,
                "title": section.title,
                "level": section.level,
                "order_index": section.order_index,
                "chunks": self._load_chunks(section.id)
            })

        return results

    def _load_chunks(self, section_id):

        chunks = (
            self.db.query(Chunk)
            .filter(Chunk.section_id == section_id)
            .order_by(Chunk.chunk_index)
            .all()
        )

        return [
            {
                "id": chunk.id,
                "content": chunk.content,
                "metadata": chunk.chunk_metadata,
            }
            for chunk in chunks
        ]

    def _context_to_text(self, context):

        text = []

        for section in context["sections"]:

            text.append(f"# {section['title']}")

            for chunk in section["chunks"]:
                text.append(chunk["content"])

            text.append("")

        return "\n".join(text)