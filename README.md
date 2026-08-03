# RecruitFlow Intelligence Engine

## Overview

RecruitFlow Intelligence Engine is an AI-powered Resume Intelligence System that automates the recruitment process by parsing resumes, extracting candidate information, analyzing profiles using Google Gemini AI, and recommending suitable job roles.

---

## Features

- Upload PDF and DOCX resumes
- Resume parsing
- Candidate information extraction
- AI-powered resume analysis
- Job role recommendation
- Suitability scoring
- MySQL database integration
- Dashboard for recruiters
- Candidate analytics with graph visualization

---

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

### Backend
- Python
- Flask
- SQLAlchemy

### Database
- SQLite / MySQL

### AI
- Google Gemini API

### Resume Parsing
- PyMuPDF
- python-docx

---

## Project Structure

```
RecruitFlow/
│
├── backend/
│   ├── app.py
│   ├── routes.py
│   ├── parser.py
│   ├── ai_engine.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── uploads/
│
├── frontend/
│   ├── index.html
│   ├── upload.html
│   ├── dashboard.html
│   ├── candidate.html
│   ├── css/
│   │      style.css
│   ├── js/
│   │      script.js
│   └── images/
│
└── README.md
```

---

## Installation

### Clone the Project

```
git clone <repository-url>
```

### Create Virtual Environment

```
python -m venv venv
```

### Activate Virtual Environment

Windows

```
venv\Scripts\activate
```

Linux / macOS

```
source venv/bin/activate
```

### Install Dependencies

```
pip install -r backend/requirements.txt
```

### Run the Backend

```
cd backend
python app.py
```
---

## Screenshots

### Resume Upload Page

(Add upload page screenshot here)

### Candidate Analysis Page

(Add candidate page screenshot here)

### Recruiter Dashboard

(Add dashboard screenshot here)

---

## Future Improvements

- Resume ranking
- Candidate search
- HR dashboard
- Interview scheduling
- ATS integration
- Skill gap analysis
- Email notifications

---

## Developed By

Lokesh Galiveti
B.Tech CSE (AIML)