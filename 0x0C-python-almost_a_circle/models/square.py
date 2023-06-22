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

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.
        """
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns dictionary representation
        of Square.
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y.": self.y
        }