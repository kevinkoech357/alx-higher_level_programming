#!/usr/bin/python3

"""
Model for a class named Base.
"""


# importing libraries
import json
import csv


class Base:
    """
    A class named Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiating Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation
        of list_objs to a file.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string(obj_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON
        string representation.
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with
        all attributes set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list = cls.from_json_string(file.read())
                return [cls.create(**item) for item in list]
        except FileNotFoundError:
            return []
