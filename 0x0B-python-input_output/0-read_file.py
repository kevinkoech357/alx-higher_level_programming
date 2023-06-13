#!/usr/bin/python3

"""
Reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Uses with statement to read filename
    and print to stdout.
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
