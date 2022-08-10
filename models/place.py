#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Place(BaseModel, Base):
    """represont a User from database
     __tablename__: the name of sql table
    city_id (sqlalchemy.String): id of city
    user_id (sqlalchemy.String): id of  user
    name (sqlalchemy.String): The name of Place
    description (sqlalchemy.String): The description of user
    number_rooms (sqlalchemy.Integer): The number_rooms in place
    number_bathrooms (sqlalchemy.Integer): The number_bathrooms in place
    max_guest (sqlalchemy.Integer: The max_guest in place
    price_by_night (sqlalchemy.Integer): The price_by_night in place
    latitude (sqlalchemy.Float): The latitude of place
    ongitude (sqlalchemy.Float): The ongitude of place
   """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
