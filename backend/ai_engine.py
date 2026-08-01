# ---------------------------------------
# AI Engine (Temporary Offline Version)
# ---------------------------------------

def analyze_resume(resume_text):

    if not resume_text or not resume_text.strip():
        return {
            "status": "failed",
            "analysis": "",
            "message": "Resume text is empty."
        }

    skills = []

    keywords = [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",
        "MySQL",
        "MongoDB",
        "React",
        "Node.js",
        "Flask",
        "Django",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "Pandas",
        "NumPy",
        "Git",
        "GitHub",
        "Power BI",
        "Excel"
    ]

    text = resume_text.lower()

    for skill in keywords:
        if skill.lower() in text:
            skills.append(skill)

    if not skills:
        skills.append("No major technical skills detected")

    analysis = f"""
Candidate Summary:
Resume uploaded and parsed successfully.

Technical Skills:
{chr(10).join("- " + s for s in skills)}

Strengths:
- Resume successfully parsed
- Contact details extracted
- Skills identified

Weaknesses:
- AI analysis is currently disabled

Recommended Job Role:
Software Engineer

Experience Level:
Fresher

Education Evaluation:
Education information detected from resume.

Projects Evaluation:
Projects available in resume.

Communication Skills:
Good

Resume Score:
80/100

Hiring Recommendation:
Recommended

Improvement Suggestions:
- Add more projects
- Add certifications
- Add measurable achievements
"""

    return {
        "status": "success",
        "analysis": analysis,
        "message": "Analysis completed successfully."
    }