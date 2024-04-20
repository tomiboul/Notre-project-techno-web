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
                          adresse=u.adresse,
                          phone=u.phone,
                          admin = u.admin,
                          blocked = u.blocked
                           
                          )
        return user
    
def get_user_by_email(email : str):
    with Session() as session:
        statement = select(User).where(User.email.like(email))
        u = session.scalar(statement)
        if u is not None:
            user = UserSchema(id=u.id, 
                            name=u.name, 
                            firstname = u.firstname, 
                            email=email, 
                            hashed_password = u.hashed_password, 
                            adresse=u.adresse,
                            phone=u.phone,
                            admin = u.admin,
                            blocked = u.blocked
                            )
            return user
        return None
def save_user(user : UserSchema) :
    with Session() as session :
        new_user = User(id=user.id,
                              name=user.name,
                              firstname=user.firstname,
                              email=user.email,
                              hashed_password=user.hashed_password,
                              adresse=user.adresse,
                              admin=user.admin,
                              phone=user.phone,
                              blocked = user.blocked
                              )
        session.add(new_user)
        session.commit()
        
def get_all_users() :
    with Session() as session :
        statement = select(User)
        users = session.scalars(statement).unique().all()
        users_list = []
        for u in users :
            users_list.append(UserSchema(id=u.id,
                                         name=u.name,
                                         firstname=u.firstname,
                                         email=u.email,
                                         phone = u.phone,
                                         admin=u.admin,
                                         adresse=u.adresse,
                                         hashed_password=u.hashed_password,
                                         blocked = u.blocked
                                         ))
            
        return users_list

def change_password(new_password, user_id) :
    with Session() as session :
        statement = select(User).where(User.id.like(user_id))
        u = session.scalar(statement)

        if u is not None :
            u.hashed_password = new_password

        session.commit()
