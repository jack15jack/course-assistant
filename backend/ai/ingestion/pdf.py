from pypdf import PdfReader


def extract_pdf_text(filepath):

    reader = PdfReader(filepath)

    text = ""

    for page_number, page in enumerate(reader.pages):

        page_text = page.extract_text()

        if page_text:
            text += (
                f"\n\n--- Page {page_number+1} ---\n"
            )

            text += page_text


    return text