#!/usr/bin/python3

"""
This module contains a function that prints a square with # symbol.
"""


def print_square(size):
    """
    Prints a square with # synbol.

    Args:
        size: Length of the square.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
