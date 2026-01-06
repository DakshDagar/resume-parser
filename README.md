# AI Resume Parser (Flask + OpenAI)

A production-grade, AI-powered resume parser built with Flask.  
Upload a resume and instantly extract clean, structured, ATS-style data using a large language model.

This project focuses on **real-world resume understanding**, not brittle keyword hacks or rigid rules.  
If this app can understand your resume, most modern ATS systems can too.

---

## 🚀 Features

- Upload resumes in **PDF, DOCX, and TXT** formats
- AI-powered extraction of structured resume data:
  - Full Name
  - Email
  - Phone Number
  - Location
  - GitHub
  - LinkedIn
  - Personal Website / Additional URLs
  - Employment History (with duration & responsibilities)
  - Technical Skills
  - Soft Skills
- Clean, readable ATS-style output
- Intelligent handling of nested experience data
- Responsive, modern UI built with **Tailwind CSS**
- Optimized for real recruiter and ATS scanning behavior

---

## 🛠 Tech Stack

### Backend
- Python
- Flask

### AI
- OpenAI API (`gpt-4o-mini`)

### File Parsing
- PDF: `pypdf`
- DOCX: `python-docx`
- TXT: native file reading

### Frontend
- HTML
- Tailwind CSS

### Configuration
- Environment variables
- Optional `config.yaml`

---

## 🧠 Why This Approach

Traditional resume parsers rely on:
- brittle keyword matching
- rigid templates
- layout-specific heuristics

This project uses a **large language model** to interpret resumes semantically, similar to how:
- a human recruiter reads resumes
- modern ATS platforms normalize candidate data

The result is:
- higher flexibility across formats  
- better handling of real-world resumes  
- cleaner structured output without manual rules  

---

## ▶️ Running Locally

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ai-resume-parser
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Set your OpenAI API key
```bash
Recommended (environment variable):
export OPENAI_API_KEY="your_api_key_here"
Or configure it in config.yaml.
```
### 4. Start the application
```bash
python app.py
```
### 5. Open in your browser
```bash
http://localhost:8000
```
### ⚠️ Notes
```bash
Text-based PDFs work best
Scanned or image-based resumes require OCR (not included yet)
OpenAI API usage requires credits
ChatGPT subscription plans do not include API access
```
### 🔮 Future Improvements
```bash
OCR support for scanned resumes
ATS score comparison against a job description
Export parsed results to JSON / CSV
Drag-and-drop uploads
Session-based history
Local LLM fallback for zero-cost parsing
```
### 👤 Author
```bash
Daksh Dagar
Portfolio project focused on practical AI integration, clean backend design, and production-ready UI.

cd ai-resume-parser

