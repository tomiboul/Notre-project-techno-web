from app.schemas.voiture import CarSchema
from fastapi import HTTPException, status
from app.database import Session
from sqlalchemy import select
from app.models.voiture import Car
#from app.schemas.users import CarSchema



def get_all_car_for_location() -> list[CarSchema]:
    with Session() as session :
        statement = select(Car) #pas oublié le where
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
                                        proprietaire_id= car.proprietaire_id
                                        ))    
        return car_location_list

