#!/usr/bin/python3

"""
Returns JSON representation of an object.
"""


# importing json
import json


def to_json_string(my_obj):
    """
    Returns:
        JSON representation of my_obj.
    """
    json_representation = json.dumps(my_obj)
    return json_representation
