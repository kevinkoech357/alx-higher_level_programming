#!/usr/bin/python3

"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int/float): First integer.
        b (int/float): Second integer.

    Raises:
        TypeError: If a or b is not an integer/float.

    Returns:
        Sum of a and b.

    Example:
        >>>add_integer(1, 1)
        >>>2
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
