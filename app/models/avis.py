from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Float
from app.database import Base
from app.models.users import User


class Avis(Base):
    __tablename__ = 'avisClient'
    avisId = mapped_column(String(37), primary_key=True)
    avis = mapped_column(String(300))
    rating = mapped_column(String(20))
    idUser :Mapped[str]=  mapped_column(ForeignKey("users.id"))

    