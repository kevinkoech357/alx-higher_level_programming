#!/usr/bin/python3

"""
A module that defines a class Student.
"""


class Student:
    """
    A class that defines student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A public method that retrieves
        dictionary representation of Student.
        """
        json = {}

        if attrs is None:
            return self.__dict__
        else:
            for attr in attrs:
                if hasattr(self, attr):
                    json[attr] = getattr(self, attr)
            return json
