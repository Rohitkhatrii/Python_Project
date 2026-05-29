from pathlib import Path
import docx2txt
from PyPDF2 import PdfReader


def extract_pdf(file_obj):
    reader = PdfReader(file_obj)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)


def extract_docx(file_obj):
    return docx2txt.process(file_obj) or ""


def extract_text(filename, file_obj):
    suffix = Path(filename).suffix.lower()
    if suffix == ".pdf":
        return extract_pdf(file_obj)
    if suffix == ".docx":
        return extract_docx(file_obj)
    raise ValueError("Unsupported file format. Please upload PDF or DOCX only.")