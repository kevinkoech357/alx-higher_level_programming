#!/usr/bin/python3

"""
Creates a class Rectangle.
"""


class Rectangle:
    """
    Represents a Rectangle object with width and height.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with width and height.

        Args:
            width (int): Width of Rectangle. Default is 0.
            height (int): Height of Rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets width of Rectangle.

        Returns:
            int: Width of the Rectangle.
        """
        return (self.__width)

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
        return (self.__height)

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

    def area(self):
        """
        Calculates area of Rectangle.

        Returns:
            int: Computed area of Rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates perimeter of Rectangle.

        Returns:
            int: Computed perimeter of Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Provides a string representation of Rectangle.

        Returns:
            Empty string if width or height = 0.
            Otherwise: Rectangle representation with #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = ""
        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        return (rectangle[:-1])

    def __repr__(self):
        """
        Provides a string representation of the rectangle
        to be used to recreate a new instance.

        Returns:
            A string representation of Rectangle.
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints Bye rectangle ... when an instance of Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares area of rect_1 and rect_2.

        Args:
            rect_1 (Rectangle): First rectangle instance.
            rect_2 (Rectangle): Second rectangle instance.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Biggest rectangle based on area.
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance with width == height == size.

        Args:
            size (int): Size of the new Rectangle. Default is 0.

        Returns:
            A new Rectangle instance akin to a square.
        """
        return (cls(size, size))
