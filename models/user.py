#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.city import City
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey


class User(BaseModel, Base):
    """represont a User from database
     __tablename__: the name of sql table
    email (sqlalchemy.String): The emial of user
    password (sqlalchemy.String): The password of user
    first_name (sqlalchemy.String): The first_name of user
    last_name (sqlalchemy.String): The last_name of user
   """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
