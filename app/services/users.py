from app.schemas.users import UserSchema
from app.database import Session
from sqlalchemy import select
from app.models.users import User

def get_user_by_id(id : str) :
    with Session() as session:
        statement = select(User).where(User.id.like(id))
        u = session.scalar(statement)

        user = UserSchema(id=id, 
                          name=u.name, 
                          firstname = u.firstname, 
                          email=u.email, 
                          hashed_password = u.hashed_password, 
                           
                          )
        return user