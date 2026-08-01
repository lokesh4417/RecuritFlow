import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# -------------------------------------------------
# Database Configuration
# -------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "recruitflow.db")

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# -------------------------------------------------
# Create Database Engine
# -------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)

# -------------------------------------------------
# Session Factory
# -------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# -------------------------------------------------
# Base Class
# -------------------------------------------------

Base = declarative_base()

# -------------------------------------------------
# Database Dependency
# -------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()