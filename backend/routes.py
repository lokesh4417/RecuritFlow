from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from parser import ResumeParser
from database import SessionLocal
from models import Candidate
from ai_engine import analyze_resume

import os

# -----------------------------
# Blueprint
# -----------------------------
api = Blueprint("api", __name__)

# -----------------------------
# Upload Folder
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

ALLOWED_EXTENSIONS = {"pdf", "docx"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# -----------------------------
# Home API
# -----------------------------
@api.route("/api", methods=["GET"])
def api_home():
    return jsonify({
        "success": True,
        "message": "RecruitFlow API is running successfully."
    })


# -----------------------------
# Upload Resume
# -----------------------------
@api.route("/upload", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({
            "success": False,
            "message": "No file uploaded."
        }), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected."
        }), 400

    if not allowed_file(file.filename):
        return jsonify({
            "success": False,
            "message": "Only PDF and DOCX files are allowed."
        }), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    # Parse Resume
    try:
        parser = ResumeParser(filepath)
        candidate = parser.parse()

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Resume parsing failed: {str(e)}"
        }), 500

    # Validation
    if not candidate.get("name"):
        return jsonify({
            "success": False,
            "message": "Candidate name not found."
        }), 400

    if not candidate.get("email"):
        return jsonify({
            "success": False,
            "message": "Email not found."
        }), 400

    # AI Analysis
    try:
        ai_result = analyze_resume(candidate.get("raw_text", ""))

    except Exception as e:
        ai_result = {
            "status": "failed",
            "message": str(e)
        }

    db = SessionLocal()

    try:

        existing = db.query(Candidate).filter(
            Candidate.email == candidate["email"]
        ).first()

        if existing:
            return jsonify({
                "success": False,
                "message": "Candidate already exists."
            }), 409

        new_candidate = Candidate(
            name=candidate.get("name"),
            email=candidate.get("email"),
            phone=candidate.get("phone"),
            skills=", ".join(candidate.get("skills", [])),
            raw_text=candidate.get("raw_text", "")
        )

        db.add(new_candidate)
        db.commit()
        db.refresh(new_candidate)

        return jsonify({
            "success": True,
            "message": "Resume uploaded successfully.",
            "candidate": {
                "id": new_candidate.id,
                "name": new_candidate.name,
                "email": new_candidate.email,
                "phone": new_candidate.phone,
                "skills": new_candidate.skills
            },
            "ai_analysis": ai_result
        })

    except Exception as e:

        db.rollback()

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:
        db.close()


# -----------------------------
# Uploaded Files
# -----------------------------
@api.route("/files", methods=["GET"])
def list_files():

    files = os.listdir(UPLOAD_FOLDER)

    return jsonify({
        "success": True,
        "total_files": len(files),
        "files": files
    })


# -----------------------------
# Candidate List
# -----------------------------
@api.route("/candidates", methods=["GET"])
def get_candidates():

    db = SessionLocal()

    try:

        candidates = db.query(Candidate).all()

        result = []

        for candidate in candidates:

            result.append({

                "id": candidate.id,
                "name": candidate.name,
                "email": candidate.email,
                "phone": candidate.phone,
                "skills": candidate.skills,
                "created_at": candidate.created_at.strftime("%Y-%m-%d %H:%M:%S")

            })

        return jsonify({
            "success": True,
            "count": len(result),
            "data": result
        })

    finally:
        db.close()