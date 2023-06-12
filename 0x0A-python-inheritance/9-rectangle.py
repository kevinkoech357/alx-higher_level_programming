#!/usr/bin/python3

"""
This module creates a subclass called Rectangle
that inherits from BaseGeometry.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns area of rectangle
        """
        self.__width * self.__height

    def __str__(self):
        """
        Returns string reprsentation of Rectangle.
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
