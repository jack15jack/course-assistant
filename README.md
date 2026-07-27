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


# Tech Stack
Backend:
- Python
- FastAPI

Database:
- PostgreSQL
- SQLAlchemy
- Pydantic

AI:
- Ollama + Llama 3.1
- Faster Whisper
- EasyOCR
- Sentence-Transformer

Frontend:
- JavaScript
- React

---


```
backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                     # FastAPI entry point
│   ├── config.py                   # Environment/configuration
│   ├── database.py                 # SQLAlchemy engine/session
│   │
│   ├── models/                     # SQLAlchemy models
│   │   ├── __init__.py         
│   │   ├── course.py           
│   │   ├── document.py         
│   │   ├── job.py
│   │   ├── document_content.py
│   │   ├── section.py
│   │   ├── chunk.py
│   │   └── artifact.py
│   │
│   ├── schemas/                    # Pydantic models
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
│   │   ├── jobs.py
│   │   └── artifacts.py
│   │
│   ├── services/                   # Business logic
│   │   ├── course_service.py
│   │   ├── document_service.py
│   │   ├── processing_service.py
│   │   ├── content_service.py
│   │   ├── section_service.py
│   │   ├── chunk_service.py
│   │   └── artifact_service.py
│   │
│   └── utils/
│       └── file_utils.py
│
├── ai/
│   ├── providers/
│   │   ├── base.py
│   │   └── ollama_provider.py
│   │
│   ├── context/
│   │   └── builder.py
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
│   │   ├── normalize.py
│   │   ├── sectioning.py
│   │   ├── chunking.py
│   │   └── embeddings.py
│   │
│   └── artifact_generators/
│       ├── notes.py
│       ├── flashcards.py
│       ├── quizzes.py
│       ├── exams.py
│       └── study_guides.py
│
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
GET    /courses                                             # List Courses
POST   /courses                                             # Create New Course
GET    /courses/{course_id}                                 # Get Course
POST   /courses/{course_id}                                 # Update Existing Course
DELETE /courses/{course_id}                                 # Delete Existing Course

POST   /documents/{course_id}                               # Upload Document
GET    /documents                                           # Get All Documents
POST   /documents/{document_id}                             # Get Document
DELETE /documents/{document_id}                             # Delete Document

GET    /jobs/{job_id}                                       # Get Job
POST   /jobs/documents/{document_id}                        # Process Document Job

POST   /artifacts/gen/{scope}/{scope_id}/{artifact_type}    # Create Document Artifact
GET    /artifacts/{artifact_id}                             # Read Artifact
DELETE /artifacts/{artifact_id}                             # Delete Artifact
GET    /artifacts/document/{document_id}                    # Read Document Artifacts
GET    /artifacts/course/{course_id}                        # Read Course Artifacts
GET    /artifacts/{artifact_id}/download                    # Download Artifact

GET    /zzz/reprocess                                       # Regenerate knowledge base
```
---

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

## Phase 3 — Ingestion (Complete)

- PDF extraction
- PowerPoint extraction
- DOCX extraction
- Plain text
- Images (OCR)
- Audio (speech-to-text)
- Video (audio extraction → speech-to-text)

## Phase 4 — Knowledge Base (Complete)

- Normalize Content
- Detect Sections
- Chunking
- Embeddings

## Phase 5 — AI Generation (Complete)

- Artifact generation (notes, study guides, formula sheets, exams)
- LLM Implementation
- markdown to PDF
- Artifact endpoints

## Phase 6 — Usability

- Reprocessing Endpoint
- Regenerating Endpoint 
- Course Level Artifacts
- Frontend UI

---

# TODO:
- Regenerate knowledge base endpoint
- Cascade Deletes
- Build the front end