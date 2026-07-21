from pptx import Presentation


def extract_ppt_text(filepath):

    presentation = Presentation(filepath)

    text = ""

    for slide_number, slide in enumerate(presentation.slides):

        text += (f"\n\n--- Slide {slide_number+1} ---\n")

        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += shape.text
                text += "\n"

    return text