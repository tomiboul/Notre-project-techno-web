from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Float
from app.database import Base
from app.models.users import User


class Avis(Base):
    __tablename__ = 'avisClient'
    avisId = mapped_column(String(37), primary_key=True)
    name = mapped_column(String(30))
    firstname = mapped_column(String(30))
    email = mapped_column(String(30))
    telephone = mapped_column(String(10)) #ex : 0467 87 90 63
    avis = mapped_column(String(300))
    étoile = mapped_column(int(5))
    idUserAvis =  mapped_column(ForeignKey("users.id"))

    