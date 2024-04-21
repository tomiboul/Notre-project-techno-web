from app.schemas.voiture import CarSchema
from fastapi import HTTPException, status
from app.database import Session
from sqlalchemy import select
from app.models.voiture import Car




def get_all_car_for_location() -> list[CarSchema]:
    with Session() as session :
        statement = select(Car)
        car_data = session.scalars(statement).unique().all()

        car_location_list = []
        for car in car_data :
            car_location_list.append(CarSchema(id=car.id, 
                                        nomModel=car.nomModel, 
                                        marque=car.marque,
                                        description=car.description,
                                        date_fabrication = car.date_fabrication,
                                        etat=car.etat,
                                        image = car.image,
                                        proprietaire_id= car.proprietaire_id,
                                        prix = car.prix,
                                        vehType=car.vehType
                                        ))    
        return car_location_list

def get_car_for_location_by_id(car_id : CarSchema): 
    with Session() as session :
        statement = select(Car).where(Car.id.like(car_id))
        carId = session.scalars(statement).unique().all()

        shearch_car = CarSchema(
                                id = car_id,
                                nomModel=carId.nomModel, 
                                marque=carId.marque,
                                description=carId.description,
                                date_fabrication = carId.date_fabrication,
                                etat=carId.etat,
                                image = carId.image,
                                proprietaire_id= carId.proprietaire_id,
                                prix = carId.prix
                                )

        return shearch_car
    

def update_car_for_location(updateCar : CarSchema):
    with Session() as session :
        statement = select(Car).where(Car.id.like(updateCar.id))
        old_car = session.scalars(statement).unique().all()

        if updateCar.id is not None:
            if updateCar.nomModel is not None and updateCar.nomModel.strip:
                old_car.nomModel = updateCar.nomModel
            if updateCar.marque is not None and updateCar.marque.strip:
                old_car.marque = updateCar.marque
            if updateCar.description is not None and updateCar.description.strip:
                old_car.description = updateCar.description
            if updateCar.date_fabrication is not None and updateCar.date_fabrication.strip:
                old_car.date_fabrication = updateCar.date_fabrication
            if updateCar.etat is not None and updateCar.etat.strip:
                old_car.etat = updateCar.etat
            if updateCar.image is not None and updateCar.image.strip:
                old_car.image = updateCar.image
            if updateCar.proprietaire_id is not None and updateCar.proprietaire_id.strip:
                old_car.proprietaire_id = updateCar.proprietaire_id
            if updateCar.prix is not None and updateCar.prix.strip:
                old_car.prix = updateCar.prix
                
        session.commit()