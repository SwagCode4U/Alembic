import os
import sys
from pathlib import Path
from logging.config import fileConfig
from dotenv import load_dotenv
from sqlalchemy import create_engine
from alembic import context

sys.path.append(str(Path(__file__).parent.parent))
load_dotenv()

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ======================== ⭐ 20 MODELS IMPORT ========================
from app.database import Base
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

target_metadata = Base.metadata

# Database URL from .env (direct, avoids ConfigParser % interpolation)
DATABASE_URL = os.getenv("DATABASE_URL")

def run_migrations_offline():
    context.configure(url=DATABASE_URL, target_metadata=target_metadata,
                      literal_binds=True,
                      dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    from sqlalchemy import create_engine
    connectable = create_engine(DATABASE_URL)
    with connectable.connect() as connection:
        context.configure(connection=connection,
                          target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
