from pathlib import Path
import re


UPLOAD_ROOT = Path("uploads")


def sanitize_filename(name: str) -> str:
    """
    Convert a string into a filesystem-safe name.
    """

    name = name.strip()

    name = re.sub(r"[^\w\s-]", "", name)

    name = re.sub(r"[\s-]+", "_", name)

    return name


def get_course_upload_directory(
    course_id: int,
    course_name: str
) -> Path:

    folder = f"{course_id}_{sanitize_filename(course_name)}"

    return UPLOAD_ROOT / folder