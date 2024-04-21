
from pydantic import BaseModel, Field, ValidationError, field_validator

class CarSchema(BaseModel) :
    id: str
    nomModel : str = Field(min_length=0, max_length=30)
    marque : str = Field(min_length=0, max_length=30)
    description: str = Field(min_length=0, max_length=300)
    date_fabrication: str= Field(min_length=0, max_length=10)
    image : str = Field(min_length=1, max_length=60) # a modif
    proprietaire_id : str 
    etat : str = Field(min_length=1,max_length=10)
    prix:str=Field(min_length=1,max_length=10)
    vehType:str=Field(min_length=1,max_length=20)

                                     