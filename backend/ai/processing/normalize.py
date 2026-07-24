import re

def normalize_text(text: str) -> str:
    if not text:
        return ""

    # normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace ("\r", "\n")

    # remove trailing spaces
    text = "\n".join(line.strip() for line in text.split("\n"))

    # collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # collapse repeated spaces
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()
