from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def markdown_to_pdf(markdown_path: str, pdf_path: str):

    with open(markdown_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    doc = SimpleDocTemplate(pdf_path)

    elements = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("# "):
            elements.append(Paragraph(f"<b>{line[2:]}</b>", styles["Heading1"]))

        elif line.startswith("## "):
            elements.append(Paragraph(f"<b>{line[3:]}</b>", styles["Heading2"]))

        elif line.startswith("### "):
            elements.append(Paragraph(f"<b>{line[4:]}</b>", styles["Heading3"]))

        else:
            elements.append(Paragraph(line, styles["BodyText"]))

    doc.build(elements)