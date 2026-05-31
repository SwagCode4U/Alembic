from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.database import Base

class Achievement(Base):
    __tablename__ = "achievements"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    title = Column(String(200))
    date_awarded = Column(Date)
    description = Column(String(500))
