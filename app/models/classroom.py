from sqlalchemy import Column, Integer, String
from app.database import Base

class Classroom(Base):
    __tablename__ = "classrooms"
    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String(20), unique=True)
    capacity = Column(Integer)
    building = Column(String(50))
