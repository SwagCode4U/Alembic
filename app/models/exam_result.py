from sqlalchemy import Column, Integer, ForeignKey, Float
from app.database import Base

class ExamResult(Base):
    __tablename__ = "exam_results"
    id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey("exams.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    marks_obtained = Column(Float)
