from app.schemas.voiture import CarSchema
from fastapi import HTTPException, status
from app.database import Session
from sqlalchemy import select
from app.models.voiture import Car
from app.schemas.voiture import CarSchema
from app.models.avis import Avis
from app.schemas.avis import avisSchema

def get_all_avis():
    with Session() as session :
        statement = select(Avis)
        avis = session.scalars(statement).unique().all()

        avisListe = []

        for a in avis :
            avisListe.append(avisSchema(avisId= a.avisId, avis=a.avis, rating= a.rating, idUser=a.idUser))

        return avisListe
    
def save_avis(a:avisSchema):
    with Session() as session:
        new_avis = Avis(avisId=a.avisId, rating=a.rating, idUser=a.idUser, avis=a.avis)

        session.add(new_avis)
        session.commit()