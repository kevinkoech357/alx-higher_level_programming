#!/usr/bin/python3

"""
Creates an Object from JSON file.
"""


# importing json
import json


def load_from_json_file(filename):
    """
    Creates an Object from JSON file.
    """
    with open(filename, "r") as file:
        json_file = file.read()
        obj = json.loads(json_file)
        return obj
