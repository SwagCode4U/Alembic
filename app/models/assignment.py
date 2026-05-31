from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.database import Base

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String(200))
    due_date = Column(Date)
    max_marks = Column(Integer, default=100)
