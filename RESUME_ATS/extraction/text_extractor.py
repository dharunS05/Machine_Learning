import pdfplumber
import fitz  # PyMuPDF
import docx
import unicodedata
import os

def normalize_text(text: str) -> str:
    if not text:
        return ""
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("\u00a0", " ")
    return text.strip()

def extract_text_from_pdf(pdf_path):
    text = ""

    # Primary: PyMuPDF (much better layout recovery)
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
    except Exception:
        pass

    # Fallback: pdfplumber
    if not text.strip():
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text += (page.extract_text() or "") + "\n"
        except Exception:
            pass

    return normalize_text(text)

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join(p.text for p in doc.paragraphs)
    return normalize_text(text)

def extract_text(file_path):
    if not os.path.exists(file_path):
        return ""

    file_path = file_path.lower()

    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return ""
