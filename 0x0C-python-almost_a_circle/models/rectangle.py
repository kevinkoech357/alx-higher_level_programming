#!/usr/bin/python3

"""
Module for class Rectangle that inherits
from class Base.
"""


from models.base import Base


class Rectangle(Base):
    """
    Subclass of Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiates Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """
        Gets width of Rectangle.

        Returns:
            int: Width of the Rectangle.
        """
        return self.__width

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
            self.__width = value

    @property
    def height(self):
        """
        Gets height of Rectangle.


        Returns:
            int: Height of the Rectangle.
        """
        return self.__height

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
            self.__height = value

    @property
    def x(self):
        """
        Retrieves x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets and validates x.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Retrieves y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets and validates y.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Returns area value of Rectangle.
        """
        return self.__width * self.__height