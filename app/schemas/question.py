from pydantic import BaseModel, Field, ValidationError, field_validator

class questionSchema(BaseModel) :
    id : str
    userId : str
    reponse : str=Field(min_length=0, max_length=300)
    question : str=Field(min_length=0,max_length=300)
