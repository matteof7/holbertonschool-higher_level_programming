#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative base
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base
    Links to the MySQL table states
    
    Attributes:
        id (int): Auto-generated, unique integer, primary key
        name (str): String with maximum 128 characters, not null
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
