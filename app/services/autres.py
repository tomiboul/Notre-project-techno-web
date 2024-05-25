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
            avisListe.append(avisSchema(avisId= a.avisId, avis=a.avis, rating= a.rating, idUser=a.idUser, idCible=a.idCible))

        return avisListe
    
def save_avis(a:avisSchema):
    with Session() as session:
        new_avis = Avis(avisId=a.avisId, rating=a.rating, idUser=a.idUser, avis=a.avis, idCible=a.idCible)

        session.add(new_avis)
        session.commit()

def get_all_car_by_keyword(keyword:str, etat:str):
    with Session() as session:
        statement = select(Car).where((Car.id.like(f"%{keyword}%")|Car.nomModel.like(f"%{keyword}%")|Car.marque.like(f"%{keyword}%")|Car.vehType.like(f"%{keyword}%"))&(Car.etat.like(etat)))
        cars = session.scalars(statement).unique().all()
        carsList = []

        for c in cars :
            carsList.append(CarSchema(id=c.id, 
                                        nomModel=c.nomModel, 
                                        marque=c.marque,
                                        description=c.description,
                                        date_fabrication = c.date_fabrication,
                                        etat=c.etat,
                                        image = c.image,
                                        proprietaire_id= c.proprietaire_id,
                                        prix=c.prix,
                                        vehType=c.vehType
                                        ))

        return carsList