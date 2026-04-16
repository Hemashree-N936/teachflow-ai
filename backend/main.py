from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
from ai_agents import generate_lesson_plan, generate_quiz

app = FastAPI()

# ✅ CORS FIX (THIS IS THE IMPORTANT PART)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


@app.get("/")
def home():
    return {"message": "TeachFlow AI Backend Running 🚀"}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = extract_text(file.file)

        if not content:
            return {"error": "Could not extract text from PDF"}

        lesson = generate_lesson_plan(content)
        quiz = generate_quiz(content)

        return {
            "lesson_plan": lesson,
            "quiz": quiz
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "Backend error handled safely"
        }