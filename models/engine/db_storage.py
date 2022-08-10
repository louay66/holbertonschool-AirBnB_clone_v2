#!/usr/bin/python3
"""Defines the DBStorage engine"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """represents a database storage engine.
         Attributes:
            __engine (sqlalchemy.Engine): The working SQLAlchemy engine
           __session (sqlalchemy.Session): The working SQLAlchemy session
        """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        instances = {}
        if cls is None:
            instances_list = self.__session.query(State).all()
            instances_list.extend(self.__session.query(City).all())
            instances_list.extend(self.__session.query(User).all())
            instances_list.extend(self.__session.query(Place).all())
            instances_list.extend(self.__session.query(Review).all())
            instances_list.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            instances_list = self.__session.query(cls)
        for instance in instances_list:
            key = f"{type(instance).__name__}.{instance.id}"
            instances[key] = instance
        return instances

    def new(self, obj):
        """" add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and initialize  new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    def close(self):
        """Close the working SQLAlchemy session"""
        self.__session.close()
