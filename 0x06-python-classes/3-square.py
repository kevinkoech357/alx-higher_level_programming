#!/usr/bin/python3

"""
To be updated later. Follow through.
"""


class Square:
    """
    Size is set to private attribute after checking if it's an int and >= 0.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        def area(self):
            """
            Computes and returns area of Square
            """
            return (self.__size * self.__size)
