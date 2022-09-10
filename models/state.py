#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel
from models.city import City
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """represont a State from database
     __tablename__: the name of sql table
    name (sqlalchemy.String): The City's name
   """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",  backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Getter attribute if it in file storage"""
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    return city
