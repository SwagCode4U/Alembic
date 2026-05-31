from sqlalchemy import Column, Integer, ForeignKey, Text, Date
from app.database import Base

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    content = Column(Text)
    submitted_date = Column(Date)
