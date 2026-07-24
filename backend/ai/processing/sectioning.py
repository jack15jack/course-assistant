import re

SECTION_PATTERNS = [
    # Markdown headings
    r"^#{1,6}\s+(.*)$",

    # Numbered sections
    r"^\d+[\.\)]\s+(.*)$",

    # All caps titles
    r"^[A-Z][A-Z\s]{3,}$",

    # Common academic headings
    r"^(Introduction|Background|Overview|Summary|Conclusion|References|Appendix)\s*$"
]


def is_section_header(line: str):

    line = line.strip()

    if not line:
        return False


    for pattern in SECTION_PATTERNS:
        if re.match(pattern, line):
            return True

    return False


def clean_section_title(line: str):

    title = line.strip()

    # Remove markdown
    title = re.sub(r"^#+\s*", "", title)

    # Remove numbering
    title = re.sub(
        r"^\d+[\.\)]\s*",
        "",
        title
    )

    return title.strip()


def detect_sections(text: str):
    """
    Splits normalized text into sections.

    Returns:
    [
        {
            "title": "...",
            "content": "...",
            "level": 1,
            "position": 0
        }
    ]
    """

    lines = text.split("\n")

    sections = []

    current_title = "Document Start"
    current_content = []

    position = 0

    for line in lines:
        if is_section_header(line):
            # save previous section
            if current_content:
                sections.append(
                    {
                        "title": current_title,
                        "content": "\n".join(current_content).strip(),
                        "level": 1,
                        "position": position
                    }
                )

                position += 1

            current_title = clean_section_title(line)
            current_content = []

        else:
            current_content.append(line)

    # final section
    if current_content:
        sections.append(
            {
                "title": current_title,
                "content": "\n".join(current_content).strip(),
                "level": 1,
                "position": position
            }
        )

    return sections