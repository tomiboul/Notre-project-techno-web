from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, Boolean
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = mapped_column(String(37), primary_key=True)
    name = mapped_column(String(30))
    firstname = mapped_column(String(30))
    email = mapped_column(String(30))
    telephone = mapped_column(String(10))
    hashed_password = mapped_column(String(32))
    admin = mapped_column(Boolean)
    # blocked = mapped_column(Boolean)