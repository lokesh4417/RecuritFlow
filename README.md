# RecruitFlow Intelligence Engine

## Overview

RecruitFlow Intelligence Engine is an AI-powered Resume Intelligence System that automates the recruitment process by parsing resumes, extracting candidate information, analyzing resumes using Google Gemini AI, and recommending suitable job roles for candidates.

---

## Features

- Upload PDF and DOCX resumes
- Resume parsing and information extraction
- AI-powered resume analysis using Google Gemini
- Candidate profile generation
- Job role recommendation
- Resume suitability scoring
- Recruiter dashboard
- Candidate analytics with graph visualization
- SQLite/MySQL database support

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

```text
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
│   ├── uploads/
│   └── recruitflow.db
│
├── frontend/
│   ├── index.html
│   ├── upload.html
│   ├── candidate.html
│   ├── dashboard.html
│   ├── css/
│   └── js/
│
├── screenshots/
│   ├── home.jpeg
│   ├── upload.jpeg
│   ├── candidate.jpeg
│   └── dashboard.jpeg
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/lokesh4417/RecuritFlow.git
cd RecuritFlow
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### Run the Backend

```bash
cd backend
python app.py
```

### Open the Frontend

Open `frontend/index.html` using **Live Server** in VS Code.

---

## Screenshots

### Home Page

![Home Page](screenshots/home.jpeg)

### Resume Upload Page

![Upload Page](screenshots/upload.jpeg)

### Candidate Analysis Page

![Candidate Page](screenshots/candidate.jpeg)

### Recruiter Dashboard

![Dashboard](screenshots/dashboard.jpeg)

---

## Future Improvements

- Resume ranking
- Candidate search and filtering
- Interview scheduling
- ATS integration
- Email notifications
- Skill gap analysis
- Multi-user authentication
- Cloud deployment

---

## Developed By

**Lokesh Galiveti**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

---

## License

This project is developed for educational and learning purposes.