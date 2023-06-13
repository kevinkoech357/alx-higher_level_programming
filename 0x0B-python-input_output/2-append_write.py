#!/usr/bin/python3

"""
Appends string to end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends string to end of text file.

    Args:
        filename: Text file involved.
        text: String to be appended.
    """
    with open(filename, "a+") as file:
        num_of_chars = file.write(text)
        return num_of_chars
