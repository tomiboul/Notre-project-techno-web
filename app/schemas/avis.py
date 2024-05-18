from pydantic import BaseModel, Field, ValidationError, field_validator

class avisSchema(BaseModel) :
    avisId : str
    idUser :  str
    avis : str=Field(min_length=0, max_length=300)
    rating : str=Field(min_length=5, max_length=20)
