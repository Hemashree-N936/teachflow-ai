# TeachFlow AI

TeachFlow AI is a teacher productivity demo built with a Next.js frontend and a FastAPI backend. Upload a PDF lesson or chapter, and the app extracts text, generates a lesson plan, and creates a quiz section using a multi-agent style workflow.

## 🚀 Features

- PDF upload interface
- Text extraction from PDF using `pdfplumber`
- Lesson plan generator
- Quiz generator
- Download generated content as PDF
- Simple, clean Next.js + Tailwind UI

## 🧱 Architecture

- `backend/`
  - `main.py` — FastAPI backend
  - `ai_agents.py` — lesson plan and quiz generator logic
- `frontend/`
  - `app/page.tsx` — React UI in Next.js
  - `next.config.ts` — Next.js configuration
  - `package.json` — frontend dependencies and scripts

## 🛠️ Stack

- Frontend
  - Next.js 16
  - React 19
  - Tailwind CSS
  - Axios
  - jsPDF
- Backend
  - Python
  - FastAPI
  - pdfplumber
  - python-multipart

## ✅ Setup

### 1. Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn pdfplumber python-multipart
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
