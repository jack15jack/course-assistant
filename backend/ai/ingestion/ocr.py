import easyocr

_reader = None

def get_ocr():
    global _reader

    if _reader is None:
        _reader = easyocr.Reader(
            ['en'],
            gpu=False
        )

    return _reader


def extract_image_text(filepath):

    ocr = get_ocr()

    results = ocr.readtext(filepath)

    contents = []

    for bbox, text, confidence in results:

        contents.append(
            {
                "content_type": "ocr",

                "content": text,

                "metadata":
                {
                    "confidence": float(confidence),
                    "source": "easyocr"
                }
            }
        )

    return contents