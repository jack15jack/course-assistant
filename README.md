# Course Assistant - AI Learning and Study Tool
- Lecture transcriber
- Textbook reader
- Note organizer
- Flashcard generator
- Practice exam generator
- Tutoring assistant
- Knowledge graph

---

# Vision
User takes notes and records the lecture audio file. 

Input: notes, lectures, lecture notes, textbook pages

The system builds detailed and organized notes/test questions on each topic.
- Lecture explanation
- Textbook definitions
- Important equations
- Example problems
- Flashcards
- Common mistakes

---

# Architecture
Inputs -> Processing Pipeline -> Course Knowledge Base -> Search or AI Generation -> Web Application


# Roadmap

## Phase 1 — Foundation (Complete)

- Database
- Courses
- Documents
- Uploads
- Migrations

## Phase 2 — Content Management (Complete)

- More document endpoints
- More course endpoints
- Update upload storage
- Update metadata
- Processing jobs
- Jobs endpoints

## Phase 3 — Ingestion

- PDF extraction
- PowerPoint extraction
- DOCX extraction
- Plain text
- Images (OCR)
- Audio (speech-to-text)
- Video (audio extraction → speech-to-text)

## Phase 4 — Knowledge Base

- Sections
- Chunking
- Embeddings
- Search

## Phase 5 — AI Generation

- Notes
- Study guides
- Formula sheets
- Practice exams
- Flashcards
- Concept maps
- Timeline generation

## Phase 6 — Intelligent Features

- Cross-document linking
- "Explain this concept"
- Exam difficulty estimation
- Weak-topic detection
- Personalized study plans
- Automatic review schedules

---

# Tech Stack
Backend:
- Python
- FastAPI

Database:
- SQLite/PostgreSQL

AI:
- Ollama + Qwen 2.5 7B
- Faster Whisper
- PaddleOCR

Frontend:
- JavaScript
- React

---


```
backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI entry point
│   ├── config.py               # Environment/configuration
│   ├── database.py             # SQLAlchemy engine/session
│   │
│   ├── models/                 # SQLAlchemy models
│   │   ├── __init__.py         
│   │   ├── course.py           
│   │   ├── document.py         
│   │   ├── section.py
│   │   ├── artifact.py
│   │   └── job.py
│   │
│   ├── schemas/                # Pydantic models
│   │   ├── __init__.py
│   │   ├── course.py
│   │   ├── document.py
│   │   ├── job.py
│   │   └── artifact.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── courses.py
│   │   ├── documents.py
│   │   ├── artifacts.py
│   │   └── jobs.py
│   │
│   ├── services/               # Business logic
│   │   ├── course_service.py
│   │   ├── document_service.py
│   │   ├── artifact_service.py
│   │   └── processing_service.py
│   │
│   └── utils/
│       └── file_utils.py
│
├── ai/
│   ├── providers/
│   │   ├── base.py
│   │   └── ollama_provider.py
│   │
│   ├── ingestion/
│   │   ├── router.py
│   │   ├── pdf.py
│   │   ├── ppt.py
│   │   ├── docx.py
│   │   ├── text.py
│   │   ├── audio.py
│   │   ├── video.py
│   │   └── ocr.py
│   │
│   ├── processing/
│   │   ├── chunking.py
│   │   ├── organization.py
│   │   ├── summarization.py
│   │   └── formulas.py
│   │
│   ├── generators/
│   │   ├── notes.py
│   │   ├── flashcards.py
│   │   ├── quizzes.py
│   │   ├── exams.py
│   │   └── study_guides.py
│   │
│   └── pipeline/
│       ├── __init__.py
│       ├── document_pipeline.py
│       ├── artifact_pipeline.py
│       ├── metadata_pipeline.py
│       └── pipeline_manager.py
│
├── uploads/
├── generated/
├── alembic/
│   ├── script.py.mako
│   ├── env.py
│   └── versions/
│
├── tests/
├── .env
└── requirements.txt
```

---
# API Endpoints

```
GET    /courses                             # List Courses
POST   /courses                             # Create New Course
GET    /courses/{course_id}                 # Get Course
POST   /courses/{course_id}                 # Update Existing Course
DELETE /courses/{course_id}                 # Delete Existing Course

POST   /documents/{course_id}               # Upload Document
GET    /documents                           # Get All Documents
POST   /documents/{document_id}             # Get Document
DELETE /documents/{document_id}             # Delete Document

GET    /jobs/{job_id}                       # Get Job
POST   /jobs/documents/{document_id}        # Process Document Job
```