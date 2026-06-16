from docx import Document

def extract_jd_text(docx_path):

    doc = Document(docx_path)

    full_text = []

    for para in doc.paragraphs:

        if para.text.strip():

            full_text.append(
                para.text
            )

    return "\n".join(full_text)
