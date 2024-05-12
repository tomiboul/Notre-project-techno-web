from app.schemas.voiture import CarSchema
from fastapi import HTTPException, status
from app.database import Session
from sqlalchemy import select
from app.models.voiture import Car
from app.schemas.voiture import CarSchema



def get_all_car_for_sale() -> list[CarSchema]:
    with Session() as session :
        statement = select(Car).where(Car.etat.like('vente')) #pas oublié le where
        car_data = session.scalars(statement).unique().all()

        car_list = []
        for car in car_data :
            car_list.append(CarSchema(id=car.id, 
                                        nomModel=car.nomModel, 
                                        marque=car.marque,
                                        description=car.description,
                                        date_fabrication = car.date_fabrication,
                                        etat=car.etat,
                                        image = car.image,
                                        proprietaire_id= car.proprietaire_id,
                                        prix=car.prix,
                                        vehType=car.vehType
                                        ))    
        return car_list

def get_id_car(car_id : str) :
    with Session() as session :
        statement = select(Car).where(Car.id.like(car_id))
        idCar = session.scalar(statement)
 
        car= CarSchema(id=idCar.id, 
                     nomModel=idCar.nomModel, 
                    marque=idCar.marque,
                    description=idCar.description,
                    date_fabrication = idCar.date_fabrication,
                    etat=idCar.etat,
                    image = idCar.image,
                    proprietaire_id= idCar.proprietaire_id,
                    vehType=idCar.vehType,
                    prix=idCar.prix
                    )   
        return car


def update_car(updateCar : CarSchema):
    with Session() as session :
        statement = select(Car).where(Car.id.like(updateCar.id))
        old_Car = session.scalar(statement)

        if old_Car is not None :
            if updateCar.id is not None and updateCar.id.strip():
                old_Car.id = updateCar.id 
            if updateCar.nomModel is not None and updateCar.nomModel.strip():
                old_Car.nomModel = updateCar.nomModel 
            if updateCar.marque is not None and updateCar.marque.strip():
                old_Car.marque = updateCar.marque 
            if updateCar.description is not None and updateCar.description.strip():
                old_Car.description = updateCar.description 
            if updateCar.date_fabrication is not None and updateCar.date_fabrication.strip():
                old_Car.date_fabrication = updateCar.date_fabrication 
            if updateCar.etat is not None and updateCar.etat.strip():
                old_Car.etat = updateCar.etat 
            if updateCar.proprietaire_id is not None and updateCar.proprietaire_id.strip():
                old_Car.proprietaire_id = updateCar.proprietaire_id 
            if updateCar.vehType is not None and updateCar.vehType.strip():
                old_Car.vehType = updateCar.vehType

        session.commit()
  
def delete_car (deleteCar : CarSchema):
    with Session() as session :
        statement = select(Car).where(Car.id.like(deleteCar.id))
        car_chose_to_delete = session.scalars(statement).unique().all()

        session.delete(car_chose_to_delete)
        session.commit()


def raise_bad_request():
    HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Changement impossible et/ou condition non respectée.",
    )

def save_car_for_sale(car:CarSchema):
    with Session() as session :
        new_car = Car(id=car.id, 
                      marque=car.marque,
                      vehType=car.vehType,
                      nomModel=car.nomModel,
                      description=car.description,
                      date_fabrication=car.date_fabrication,
                      etat = car.etat,
                      image = car.image,
                      proprietaire_id= car.proprietaire_id,
                      prix=car.prix
        )
        session.add(new_car)
        session.commit()


def car_sold(id:str):
    with Session() as session :
        statement = select(Car).where(Car.id.like(id))
        car = session.scalar(statement)

        car.etat = 'vendu'
        session.commit()