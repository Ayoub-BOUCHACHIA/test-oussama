
import fitz  # PyMuPDF
from docx import Document

PDF = 'pdf'
DOCX = 'docx'

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    doc.close()
    return text

def parse_path(path):
    file_name = path.split('/')[-1]
    ext = file_name.split('.')[-1]
    ipp, iddocument = file_name.replace('.'+ext, '').split('_')
    return int(ipp), int(iddocument), ext.lower()

def read_and_pars_all_files(list_paths):
    data = []
    for path in list_paths:
        ipp, iddocument, ext = parse_path(path)

        if ext == PDF:
            text_content = extract_text_from_pdf(path)
        if  ext == DOCX:
            text_content = extract_text_from_docx(path)

        data.append([
            ipp,
            iddocument,
            ext,
            text_content
        ])

    return data

