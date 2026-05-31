from sqlalchemy import Column, Integer, ForeignKey, Date
from app.database import Base

class BookIssue(Base):
    __tablename__ = "book_issues"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("library_books.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    issue_date = Column(Date)
    return_date = Column(Date)
