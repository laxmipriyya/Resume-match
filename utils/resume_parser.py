import pdfminer.high_level
import docx

def extract_text_from_resume(file):
    if file.filename.endswith(".pdf"):
        return pdfminer.high_level.extract_text(file)
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""
