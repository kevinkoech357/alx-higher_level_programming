#!/usr/bin/python3

"""
Creates a class Rectangle.
"""


class Rectangle:
    """
    Initializes an instance of Rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with width and height.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Returns width.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of Rectangle.
        Performs some checks in lieu with set exceptions.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """
        Returns height.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets height of Rectangle.
        Performs some checks in lieu with set exceptions.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
