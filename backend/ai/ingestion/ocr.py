from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

def extract_image_text(filepath):

    results = []

    output = ocr.predict(filepath)

    for page in output:

        for text, score in zip(
            page["rec_texts"],
            page["rec_scores"]
        ):
            results.append(
                {
                    "content_type": "ocr",
                    "content": text,
                    "content_metadata": {
                        "confidence": float(score),
                        "source": "paddleocr"
                    }
                }
            )

    return results