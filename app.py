import os
from flask import Flask, request, render_template
from pypdf import PdfReader
from docx import Document
from resumeparser.ats_extractor import ats_extractor

UPLOAD_PATH = "_DATA_"
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}

app = Flask(__name__)
os.makedirs(UPLOAD_PATH, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_resume():
    file = request.files.get("pdf_doc")

    if not file or file.filename == "":
        return "No file uploaded", 400

    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        return f"Unsupported file type: {ext}", 400

    file_path = os.path.join(UPLOAD_PATH, f"resume{ext}")
    file.save(file_path)

    if ext == ".pdf":
        resume_text = extract_text_from_pdf(file_path)
    elif ext == ".docx":
        resume_text = extract_text_from_docx(file_path)
    elif ext == ".txt":
        resume_text = extract_text_from_txt(file_path)
    else:
        return "Unsupported file format", 400

    if not resume_text.strip():
        return "Could not extract text from the resume", 400

    parsed_data = ats_extractor(resume_text)

    return render_template("index.html", data=parsed_data)


def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)


def extract_text_from_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


if __name__ == "__main__":
    app.run()
