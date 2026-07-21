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

## Phase 1 - Document Assistant
Upload PDFs and ask questions

- PDF upload
- text extraction
- chunking
- embeddings
- semantic research
- chat interface

## Phase 2 - Lecture Audio Processing
Lecture recording -> speech-to-text -> transcript -> knowledge extraction

- automatic lecture notes
- important concepts
- definitions
- equations

## Phase 3 - Study Material Generator
Generate flashcards, practice problems, study guide, formula sheet

## Phase 4 - Adaptive Learning
Track user knowledge and plan learning accordingly
---

# Tech Stack
Backend:
- Python
- FastAPI

Database:
- SQLite/PostgreSQL

AI:
- OpenAI API or local model

Frontend:
- JavaScript
- React

Other:
- Whisper

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
│   │   └── pipeline_service.py
│   │
│   └── utils/
│       └── file_utils.py
│
├── ai/
│   ├── providers/
│   │   ├── base.py
│   │   ├── openai_provider.py
│   │   └── local_provider.py
│   │
│   ├── ingestion/
│   │   ├── pdf.py
│   │   ├── ppt.py
│   │   ├── audio.py
│   │   └── notes.py
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
│   └── pipeline.py
│
├── uploads/
├── generated/
├── alembic/
│   └── env.py
├── tests/
├── .env
└── requirements.txt
```

---
# API Endpoints

GET    /courses
POST   /courses
GET    /courses/{id}
DELETE /courses/{id}

POST   /courses/{id}/documents
GET    /courses/{id}/documents
DELETE /documents/{id}

POST   /courses/{id}/process

GET    /courses/{id}/artifacts
GET    /artifacts/{id}
PUT    /artifacts/{id}
