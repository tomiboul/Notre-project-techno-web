from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
#from app.models.users import User
from sqlalchemy import select

engine = create_engine("sqlite:///data/db.sqlite", echo=True)
Session = sessionmaker(engine)
session = Session()

class Base(DeclarativeBase):
    pass



def create_database():
    #from app.models.users import User   
    #from app.models.books import Book
    Base.metadata.create_all(engine)
   

    #mdp compte Louis : 'bomel'
    #mdp compte Thomas  : 'skibidi'
    #mdp compte admin : 'admin'

    #default_users = session.query(User).filter(User.email.in_(["louisbomal@outlook.com", "thomasbusoni@gmail.com", "admin"])).all()
    #default_books = session.query(Book).all()
    #default_users = [User(id=str(uuid4()),email="louisbomal@outlook.com", name="Bomal",firstname="Louis",hashed_password="7b3e24324eb3401229ea53300fb998e27185e8b4abc1a46b03aa51a8e00aa3bb", admin=True, blocked = False),
    #                 User(id=str(uuid4()),email="thomasbusoni@gmail.com", name="Busoni",firstname="Thomas",hashed_password="1bb56293f6dc4311f60a4a0173a5aafaa8ccc46affa067783538963476501afb", admin=True, blocked = False),
    #                 User(id=str(uuid4()),email="admin", name="admin",firstname="admin",hashed_password="fb001dfcffd1c899f3297871406242f097aecf1a5342ccf3ebcd116146188e4b", admin=True, blocked = False)]
    
    #for user in default_users:
    #    session.delete(user)
    
    #for book in default_books:
    #    session.delete(book)
    
    """
    default_books = [Book(id=str(uuid4()), nom='Star Wars', auteur='George Lucassetout', editeur='lucasbooks', description='bateaux volants qui tirent des lasers c fou', date_creation='20-03-2002', proprietaire_id='26fc696c-bbc9-4c89-bdb6-baa9eebcd446', proprietaire=session.query(User).get('26fc696c-bbc9-4c89-bdb6-baa9eebcd446')),
                     Book(id=str(uuid4()), nom='dictionnaire édition 1987', auteur='George Washington', editeur='larousse', description='bateaux volants qui tirent des lasers c fou', date_creation='31-07-2017', proprietaire_id='26fc696c-bbc9-4c89-bdb6-baa9eebcd446', proprietaire=session.query(User).get('26fc696c-bbc9-4c89-bdb6-baa9eebcd446')),
                     Book(id=str(uuid4()), nom='Lancé de thomates', auteur='Tomiboul', editeur='letoms', description='Thomas joue au baseball', date_creation='20-01-2090', proprietaire_id='2df8430a-982f-4e59-a824-59196df0f5a3', proprietaire=session.query(User).get('2df8430a-982f-4e59-a824-59196df0f5a3'))]
    """
    #session.add_all(default_books)
    
    #session.add_all(default_users)
    
    #session.commit()
    

def delete_database():
    Base.metadata.clear()