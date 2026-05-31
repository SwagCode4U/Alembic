from sqlalchemy import Column, Integer, String
from app.database import Base

class Coo(Base):
    __tablename__ = "coo"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), unique=True)
    credits = Column(Integer, default=3)
