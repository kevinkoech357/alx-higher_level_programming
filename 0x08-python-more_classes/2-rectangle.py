#!/usr/bin/python3

"""
Creates a class Rectangle.
"""


class Rectangle:
    """
    Represents a Rectangle object with width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with width and height.

        Args:
            width (int): Width of Rectangle. Default is 0.
            height (int): Height of Rectangle. Default is 0.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Gets width of Rectangle.

        Returns:
            int: Width of the Rectangle.
        """
        return (self._width)

    @width.setter
    def width(self, value):
        """
        Sets the width of Rectangle.

        Args:
            value (int): The width value to assign/set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
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
        Gets height of Rectangle.


        Returns:
            int: Height of the Rectangle.
        """
        return (self._height)

    @height.setter
    def height(self, value):
        """
        Sets height of Rectangle.

        Args:
            value (int): The height value to assign/set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """
        Calculates area of Rectangle.

        Returns:
            int: Computed area of Rectangle.
        """
        return (self._width * self._height)

    def perimeter(self):
        """
        Calculates perimeter of Rectangle.

        Returns:
            int: Computed perimeter of Rectangle.
        """
        return (2 * (self._width + self._height))
