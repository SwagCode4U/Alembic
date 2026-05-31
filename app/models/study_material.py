from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.database import Base

class StudyMaterial(Base):
    __tablename__ = "study_materials"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String(200))
    file_type = Column(String(20))
    description = Column(Text)
