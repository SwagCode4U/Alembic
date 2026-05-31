from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    date_of_birth = Column(Date)
    class_name = Column(String(20))
