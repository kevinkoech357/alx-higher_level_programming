#!/usr/bin/python3

# importing json
import json

"""
Returns JSON representation of an object.
"""


def to_json_string(my_obj):
    """
    Returns:
        JSON representation of my_obj.
    """
    json_representation = json.dumps(my_obj)
    return json_representation
