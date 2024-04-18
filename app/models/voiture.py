from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Float
from app.database import Base
from app.models.users import User

class Car(Base):
    __tablename__ = 'car'
    id = mapped_column(String(100), primary_key=True)
    nomModel = mapped_column(String(100))
    marque = mapped_column(String(100))
    description = mapped_column(String(200)) 
    date_fabrication = mapped_column(String(10))
    etat = mapped_column(String(100))
    image = mapped_column(String(100)) # a changer
    proprietaire_id : Mapped[str] = mapped_column(ForeignKey("users.id"))
    # proprio garage ou personne (en location proprio temporaire ou alors vente)