#!/usr/bin/python3

"""
A function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Args:
        obj: Object to be checked.

    Return:
        List of available attributes and methods of obj.
    """
    return dir(obj)
