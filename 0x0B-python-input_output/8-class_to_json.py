#!/usr/bin/python3

"""
Returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Args:
        obj: An instance of class.

    Returns:
        Dictionary description
    """
    dictionary = {}
    if hasattr(obj, "__dict__"):
        dictionary = obj.__dict__.copy()
    return dictionary
