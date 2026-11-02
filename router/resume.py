from fastapi import APIRouter, UploadFile, File, Form
from service.resume import get_answers
from PyPDF2 import PdfReader
from io import BytesIO 
from schema.resume import Improve, Tailor, AtsScore
from docx import Document


chat_router = APIRouter(
    prefix="/resume"
)

def extract_text(file_content: bytes, filename) -> str:
    try:
        if filename.endswith('.pdf'):
            reader = PdfReader(BytesIO(file_content))
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
        elif filename.endswith('.docx'):
            document = Document(BytesIO(file_content))
            text = ""
            for paragraph in document.paragraphs:
                text += paragraph.text + "\n"
            return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""


@chat_router.post("/improve")
def get_request(file: UploadFile = File(...), instructions: str = Form(...)):
    resume = extract_text(file.file.read(), file.filename)

    data = Improve(instructions=instructions)

    question = f" Accept a resume: {resume} and user instructions {data.instructions}, then return improved resume text."
    anwser = get_answers(question)

    return {
        "question" : question,
        "answer" : anwser,
        "message": "Success"
    }


@chat_router.post("/tailor")
def get_request(file: UploadFile = File(...), job_description: str = Form(...)):
    resume = extract_text(file.file.read(), file.filename)

    data = Tailor(job_description=job_description)

    question = f"Tailor the resume: {resume} according to this job description: {data.job_description}."

    anwser = get_answers(question)
    return {
        "question" : question,
        "answer" : anwser,
        "message": "Success"
    }


@chat_router.post("/ats-score")
def ats_score(file: UploadFile = File(...), job_description: str = Form(...)):
    resume = extract_text(file.file.read(), file.filename)

    data = AtsScore(job_description=job_description)

    question = f"Please provide an ATS score out of 100 with feedback for the following resume: {resume} and job description: {data.job_description}. Please provide a brief explanation for the score. Support both general and job-specific scoring."

    anwser = get_answers(question)
    return {
        "question" : question,
        "answer" : anwser,
        "message": "Success"
    }
