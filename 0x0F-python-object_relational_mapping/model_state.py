#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines a class State which is an instance
of Base=declarative_base()
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv


# Crete an instance of declarative_base
Base = declarative_base()

class State(Base):
    """
    Class state which inherits from Base.

    Has id and name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)

# Creating a connection to database
engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
