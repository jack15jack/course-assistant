from ai.ingestion.pdf import extract_pdf_text
from ai.ingestion.ppt import extract_ppt_text
from ai.ingestion.docx import extract_docx_text
from ai.ingestion.text import extract_text


def extract_document(
    filepath: str,
    file_type: str
):

    if file_type == "application/pdf":
        return extract_pdf_text(filepath)


    elif file_type in [
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "application/vnd.ms-powerpoint"
    ]:
        return extract_ppt_text(filepath)


    elif file_type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]:
        return extract_docx_text(filepath)


    elif file_type.startswith("text/"):
        return extract_text(filepath)


    else:
        raise ValueError(
            f"Unsupported file type: {file_type}"
        )