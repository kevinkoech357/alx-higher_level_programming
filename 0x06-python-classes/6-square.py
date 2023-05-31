#!/usr/bin/python3

"""
Defines a class called Square.
"""


class Square:
    """
    Square representation.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates a new square.

        Args:
            size: Size of the square.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Gets current position of Square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Sets position of Square.
        """
        if type(value) != tuple:
            raise TypeError
            print("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError
            print("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError
            print("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError
            print("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Computes and returns area of Square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints the square with # symbol.
        """
        if self.__size == 0:
            print()
        else:
            for index in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
