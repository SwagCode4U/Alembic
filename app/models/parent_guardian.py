from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class ParentGuardian(Base):
    __tablename__ = "parent_guardians"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    name = Column(String(100))
    relationship = Column(String(20))
    phone = Column(String(20))
    email = Column(String(100))
