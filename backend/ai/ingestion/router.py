from pathlib import Path

from ai.ingestion.pdf import extract_pdf_text
from ai.ingestion.docx import extract_docx_text
from ai.ingestion.ppt import extract_ppt_text
from ai.ingestion.text import extract_text
from ai.ingestion.ocr import extract_image_text
from ai.ingestion.audio import extract_audio_text
from ai.ingestion.video import extract_video_text


def extract_document(filepath, file_type):


    if file_type == "application/pdf":
        return extract_pdf_text(filepath)

    elif file_type.startswith("image"):
        return extract_image_text(filepath)

    elif file_type.startswith("audio"):
        return extract_audio_text(filepath)

    elif file_type.startswith("video"):
        return extract_video_text(filepath)

    elif file_type == "text/plain":
        return extract_text(filepath)

    elif file_type.endswith(
        "wordprocessingml.document"
    ):
        return extract_docx_text(filepath)

    elif file_type.endswith(
        "presentationml.presentation"
    ):
        return extract_ppt_text(filepath)

    raise Exception(
        f"Unsupported file type: {file_type}"
    )