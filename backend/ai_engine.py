import google.generativeai as genai
from config import GEMINI_API_KEY

# ---------------------------------------
# Configure Gemini API
# ---------------------------------------

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Please add it to config.py")

genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")


# ---------------------------------------
# Resume Analysis
# ---------------------------------------

def analyze_resume(resume_text):

    if not resume_text.strip():
        return {
            "status": "failed",
            "message": "Resume text is empty."
        }

    prompt = f"""
You are an expert HR Recruiter and Talent Acquisition Specialist.

Analyze the following resume and provide a professional evaluation.

Return the response in the following format.

--------------------------------------------------

Candidate Summary:
(3-5 lines)

Technical Skills:
- Skill 1
- Skill 2
- Skill 3

Strengths:
- Strength 1
- Strength 2
- Strength 3

Weaknesses:
- Weakness 1
- Weakness 2

Recommended Job Role:

Experience Level:
(Fresher / Junior / Mid-Level / Senior)

Education Evaluation:

Projects Evaluation:

Communication Skills:
Excellent / Good / Average

Resume Score:
__/100

Hiring Recommendation:
Highly Recommended / Recommended / Consider / Not Recommended

Improvement Suggestions:
- Suggestion 1
- Suggestion 2
- Suggestion 3

--------------------------------------------------

Resume:

{resume_text}

Only return the evaluation in the specified format.
"""

    try:

        response = model.generate_content(prompt)

        if not response or not response.text:
            return {
                "status": "failed",
                "message": "No response received from Gemini."
            }

        return response.text.strip()

    except Exception as e:

        return {
            "status": "failed",
            "message": str(e)
        }