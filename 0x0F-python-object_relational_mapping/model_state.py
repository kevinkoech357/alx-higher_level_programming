#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines a class State which is an instance
of Base=declarative_base()
"""

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class state which inherits from Base.

    Has id and name
    """

    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, nullable=False,
        unique=True, autoincrement=True
    )
    name = Column(String(255), nullable=False)
