#!/usr/bin/python3

"""
Model for a class named Base.
"""


# importing libraries
import json
import csv


class Base:
    """
    A class named Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiating Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
