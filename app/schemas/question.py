from pydantic import BaseModel, Field, ValidationError, field_validator

class Question(BaseModel) :
    questionId : str
    userId : str
    reponse : str=Field(min_length=0, max_length=300)
