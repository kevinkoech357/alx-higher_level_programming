#!/usr/bin/python3

"""
Creates a new subclass that inherits
from Rectangle.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A subclass that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns area of Square.
        """
        return self.__size ** 2
