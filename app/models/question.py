from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, Boolean
from app.database import Base


class Question(Base):
    __tablename__ = 'questions'
    id = mapped_column(String(37), primary_key=True)
    name = mapped_column(String(30))
    firstname = mapped_column(String(30))
    email = mapped_column(String(30))
    telephone = mapped_column(String(10)) #ex : 0467 87 90 63
    hashed_password = mapped_column(String(32))
    questionPosee = mapped_column(String(300))