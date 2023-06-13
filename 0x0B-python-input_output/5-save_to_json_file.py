#!/usr/bin/python3

"""
Writes an object to a text file,
using JSON representation
"""


# importing json
import json


def save_to_json_file(my_obj, filename):
    """
    Write my_obj to filename using
    JSON representation
    """
    with open(filename, "w+") as file:
        json_representation = json.dumps(my_obj)
        file = file.write(json_representation)
