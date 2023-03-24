#!/usr/bin/python3
"""New engine"""
from models.user import User
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """Class used to manage the MySQL database for the HBNB project"""
    __engine = None
    __session = None

    def __init__(self):
        """Creation of a new instance"""
        user = getenv('HBNB_MYSQL_USER')
        psw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{psw}@{host}/{db}')

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.dop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects of the specified class, or all objects
        if no class is specified"""
        objs_d = {}
        clases = {User, State, City, Amenity, Place, Review}

        if cls:
            if cls in clases:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f"{type(obj).__name__}.{obj.id}"
                    obj.__dict[key] = obj
            else:
                return objs_d
        else:
            for cls in clases:
                obj = self.__session.query(cls).all()
                for obj in objs:
                    key = f"{type(obj).__name__}.{obj.id}"
                    obj.__dict[key] = obj
        return objs_d

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Create tables and the current database session"""
        Base.metadata.create_all(self.__engine)
        session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = session
