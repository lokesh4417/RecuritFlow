import fitz
import docx
import re
import os


class ResumeParser:

    def __init__(self, filepath):
        self.filepath = filepath
        self.text = ""

    # -------------------------
    # Read PDF
    # -------------------------
    def read_pdf(self):

        document = fitz.open(self.filepath)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text.strip()

    # -------------------------
    # Read DOCX
    # -------------------------
    def read_docx(self):

        document = docx.Document(self.filepath)

        text = ""

        for para in document.paragraphs:
            if para.text.strip():
                text += para.text.strip() + "\n"

        return text.strip()

    # -------------------------
    # Extract Text
    # -------------------------
    def extract_text(self):

        extension = os.path.splitext(self.filepath)[1].lower()

        if extension == ".pdf":
            self.text = self.read_pdf()

        elif extension == ".docx":
            self.text = self.read_docx()

        else:
            raise Exception("Unsupported file format. Only PDF and DOCX are supported.")

        return self.text

    # -------------------------
    # Extract Email
    # -------------------------
    def extract_email(self):

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            self.text
        )

        return emails[0] if emails else ""

    # -------------------------
    # Extract Phone Number
    # -------------------------
    def extract_phone(self):

        phones = re.findall(
            r"(?:\+91[-\s]?)?[6-9]\d{9}",
            self.text
        )

        return phones[0] if phones else ""

    # -------------------------
    # Extract Name
    # -------------------------
    def extract_name(self):

        lines = self.text.split("\n")

        for line in lines:

            line = line.strip()

            if (
                len(line.split()) >= 2
                and len(line) < 40
                and not any(char.isdigit() for char in line)
                and "@" not in line
            ):
                return line.title()

        return ""

    # -------------------------
    # Extract Skills
    # -------------------------
    def extract_skills(self):

        skills_db = [

            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript",
            "HTML",
            "CSS",
            "React",
            "Node.js",
            "Flask",
            "Django",
            "SQL",
            "MySQL",
            "PostgreSQL",
            "MongoDB",
            "Git",
            "GitHub",
            "Machine Learning",
            "Deep Learning",
            "Data Analysis",
            "Pandas",
            "NumPy",
            "TensorFlow",
            "Power BI",
            "Excel"

        ]

        found = []

        text_lower = self.text.lower()

        for skill in skills_db:

            if skill.lower() in text_lower:
                found.append(skill)

        return sorted(list(set(found)))

    # -------------------------
    # Final Parsed Data
    # -------------------------
    def parse(self):

        self.extract_text()

        return {

            "name": self.extract_name(),
            "email": self.extract_email(),
            "phone": self.extract_phone(),
            "skills": self.extract_skills(),
            "raw_text": self.text

        }