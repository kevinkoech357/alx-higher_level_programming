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