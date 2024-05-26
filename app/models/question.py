from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey
from app.database import Base


class Question(Base):
    __tablename__ = 'questions'
    id = mapped_column(String(37), primary_key=True)
    userId :  Mapped[str] = mapped_column(ForeignKey("users.id"))
    question = mapped_column(String(300))
    reponse=mapped_column(String(300))
