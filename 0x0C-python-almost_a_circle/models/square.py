#!/usr/bin/python3

"""
Module for class Square
that inherits from Rectangle.
"""


# importing
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Retrieves size from Rectangle.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets and validates from class Rectangle.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation
        of the instance of Square.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        ))