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

    output = ocr.readtext(filepath)

    text_parts = []

    metadata = {
        "source": "easyocr",
        "regions": []
    }

    for bbox, text, confidence in output:

        text_parts.append(text)

        metadata["regions"].append(
            {
                "text": text,
                "confidence": confidence,
                "bbox": bbox
            }
        )

    return [
        {
            "content_type": "ocr",
            "content": "\n".join(text_parts),
            "metadata": metadata
        }
    ]