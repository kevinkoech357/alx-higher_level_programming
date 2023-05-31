#!/usr/bin/python3

"""
Defines a class called Square.
"""


class Square:
    """
    Square representation.
    """
    def __init__(self, size=0):
        """
        Instantiates a new square.

        Args:
            size: Size of the square.
        """

        self.size = size

    @property
    def size(self):
        """
        Retrieves current size of Square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets current size of Square.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns area of Square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints the square with # symbol.
        """
        for index in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
