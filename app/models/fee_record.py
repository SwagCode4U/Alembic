from sqlalchemy import Column, Integer, ForeignKey, Float, Date, String
from app.database import Base

class FeeRecord(Base):
    __tablename__ = "fee_records"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    amount = Column(Float)
    due_date = Column(Date)
    paid_date = Column(Date)
    status = Column(String(20), default="pending")
