#!/usr/bin/python3

"""
This module contains a function that prints one's fullname.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first_name and last_name.

    Args:
        first_name: First name.
        last_name: Last name.

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
