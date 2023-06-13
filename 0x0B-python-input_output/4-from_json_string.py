#!/usr/bin/python3

"""
Returns an object represented by JSON string.
"""


# importing json
import json


def from_json_string(my_str):
    """
    Returns:
        Python object represented by
        JSON string
    """
    object = json.loads(my_str)
    return object
