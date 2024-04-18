from pydantic import BaseModel, Field, ValidationError, field_validator

class UserSchema(BaseModel) :
    id: str
    name : str = Field(min_length=0, max_length=30)
    firstname : str = Field(min_length=0, max_length=30)
    email: str = Field(min_length=0, max_length=30)
    hashed_password: str
    adresse : str = Field(min_length=0, max_length=64)