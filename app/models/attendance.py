from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from app.database import Base

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    date = Column(Date)
    present = Column(Boolean, default=True)
