from docx import Document

def extract_docx_text(filepath):

    doc = Document(filepath)

    text = ""

    for paragraph in doc.paragraphs:

        if paragraph.text.strip():

            text += paragraph.text
            text += "\n"

    return text