from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class ClubMembership(Base):
    __tablename__ = "club_memberships"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    club_name = Column(String(100))
    role = Column(String(50))
