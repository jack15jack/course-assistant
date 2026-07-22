from pypdf import PdfReader


def extract_pdf_text(filepath):

    reader = PdfReader(filepath)

    pages = []


    for index, page in enumerate(reader.pages):

        text = page.extract_text()

        if text.strip():

            pages.append(
                {
                    "content": text,
                    "content_type": "text",
                    "metadata": {
                        "page": index + 1,
                        "location": filepath
                    }
                }
            )

    return pages