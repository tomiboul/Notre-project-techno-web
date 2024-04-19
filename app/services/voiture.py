from app.schemas.voiture import CarSchema
from fastapi import HTTPException, status
from app.database import Session
from sqlalchemy import select
from app.models.voiture import Car
from app.schemas.voiture import CarSchema



def get_all_car_for_rent() -> list[CarSchema]:
    with Session() as session :
        statement = select(Car) #pas oublié le where
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
                                        proprietaire_id= car.proprietaire_id
                                        ))    
        return car_list

def get_id_car(car_id : str) :
    with Session() as session :
        statement = select(Car).where(Car.id.like(car_id))
        idCar = session.scalars(statement).unique().all()

        car_list_id = []
        for car in idCar :
            car_list_id.append(CarSchema(id=car.id, 
                                        nomModel=car.nomModel, 
                                        marque=car.marque,
                                        description=car.description,
                                        date_fabrication = car.date_fabrication,
                                        etat=car.etat,
                                        image = car.image,
                                        proprietaire_id= car.proprietaire_id
                                        ))    
        return car_list_id


def update_car(updateCar : CarSchema):
    with Session() as session :
        statement = select(Car).where(Car.id.like(updateCar.id))
        old_Car = session.scalars(statement).unique().all()

        if old_Car is not None :
            if updateCar.id is not None and update_car.id.strip():
                old_Car.id = updateCar.id 
            if updateCar.nomModel is not None and update_car.nomModel.strip():
                old_Car.nomModel = updateCar.nomModel 
            if updateCar.marque is not None and update_car.marque.strip():
                old_Car.marque = updateCar.marque 
            if updateCar.description is not None and update_car.description.strip():
                old_Car.description = updateCar.description 
            if updateCar.date_fabrication is not None and update_car.date_fabrication.strip():
                old_Car.date_fabrication = updateCar.date_fabrication 
            if updateCar.etat is not None and update_car.etat.strip():
                old_Car.etat = updateCar.etat 
            if updateCar.image is not None and update_car.image.strip():
                old_Car.image = updateCar.image 
            if updateCar.proprietaire_id is not None and update_car.proprietaire_id.strip():
                old_Car.proprietaire_id = updateCar.proprietaire_id 
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