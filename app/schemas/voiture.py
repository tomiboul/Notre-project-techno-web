
from pydantic import BaseModel, Field, ValidationError, field_validator

class CarSchema(BaseModel) :
    id: str
    nomModel : str = Field(min_length=0, max_length=30)
    marque : str = Field(min_length=0, max_length=30)
    description: str = Field(min_length=0, max_length=300)
    date_fabrication: str= Field(min_length=0, max_length=10)
    etat : str = Field(min_length=0, max_length=15)
    image : str # a modif
    proprietaire_id : str 

                                     