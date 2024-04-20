from pydantic import BaseModel, Field, ValidationError, field_validator

class UserSchema(BaseModel) :
    id: str
    name : str = Field(min_length=0, max_length=30)
    firstname : str = Field(min_length=0, max_length=30)
    email: str = Field(min_length=0, max_length=50)
    hashed_password: str
    adresse : str = Field(min_length=0, max_length=64)
    admin : bool
    phone : str=Field(min_length=0, max_length=14)
    blocked : bool

   