from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.database import Base

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    grade = Column(String(2))
    percentage = Column(Float)
