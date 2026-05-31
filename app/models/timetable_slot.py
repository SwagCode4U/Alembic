from sqlalchemy import Column, Integer, ForeignKey, String, Time
from app.database import Base

class TimetableSlot(Base):
    __tablename__ = "timetable_slots"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    classroom_id = Column(Integer, ForeignKey("classrooms.id"))
    day_of_week = Column(String(10))
    start_time = Column(Time)
    end_time = Column(Time)
