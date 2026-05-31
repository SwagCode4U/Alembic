"""
🚀 LEARNSMART — Alembic Demo App
20 tables dikhata hai — Alembic kitni powerful hai!
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fastapi import FastAPI
from app.database import engine, Base

# === Saare 20 models import karo (taaki Base.metadata unhe jaane) ===
from app.models.student import Student
from app.models.course import Course

from app.models.teacher import Teacher
from app.models.classroom import Classroom
from app.models.enrollment import Enrollment
from app.models.assignment import Assignment
from app.models.submission import Submission
from app.models.grade import Grade
from app.models.attendance import Attendance
from app.models.exam import Exam
from app.models.exam_result import ExamResult
from app.models.library_book import LibraryBook
from app.models.book_issue import BookIssue
from app.models.fee_record import FeeRecord
from app.models.timetable_slot import TimetableSlot
from app.models.announcement import Announcement
from app.models.study_material import StudyMaterial
from app.models.achievement import Achievement
from app.models.parent_guardian import ParentGuardian
from app.models.club_membership import ClubMembership

from app.models.coo import Coo

app = FastAPI(title="LearnSmart 🎓 — Alembic Demo")

@app.on_event("startup")
def init_db():
    Base.metadata.create_all(bind=engine)
    print(f"✅ Tables ready! Total models: {len(Base.metadata.tables)}")

@app.get("/")
def root():
    return {
        "app": "LearnSmart 🎓",
        "total_models": len(Base.metadata.tables),
        "tables": list(Base.metadata.tables.keys()),
        "message": "Alembic demo ready! 🚀"
    }

@app.get("/counts")
def table_counts():
    from app.database import SessionLocal
    db = SessionLocal()
    result = {}
    for name, table in Base.metadata.tables.items():
        count = db.execute(table.select()).fetchall()
        result[name] = len(count)
    db.close()
    return {"row_counts": result}
