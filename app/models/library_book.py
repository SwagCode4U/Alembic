from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class LibraryBook(Base):
    __tablename__ = "library_books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    author = Column(String(100))
    isbn = Column(String(20), unique=True)
    available = Column(Boolean, default=True)
