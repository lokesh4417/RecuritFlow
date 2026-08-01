from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime


class Candidate(Base):
    __tablename__ = "candidates"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Candidate Details
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True)

    # Resume Details
    skills = Column(Text, nullable=True)
    raw_text = Column(Text, nullable=True)

    # Record Creation Time
    created_at = Column(DateTime, default=datetime.utcnow)