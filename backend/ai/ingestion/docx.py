from docx import Document


def extract_docx_text(filepath):

    doc = Document(filepath)

    text = "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )

    return [
        {
            "content": text,
            "content_type": "text",
            "metadata": {
                "location": filepath
            }
        }
    ]