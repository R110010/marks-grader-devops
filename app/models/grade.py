from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db.base import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    average = Column(Float)
    grade = Column(String)