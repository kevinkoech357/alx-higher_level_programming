#!/usr/bin/python3

"""
Writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes text to filename.

    Args:
        filename: Text file to written into.
        text: String to be written.
    Returns:
        Number of characters written.
    """
    with open(filename, "w+") as file:
        num_of_chars = file.write(text)
        return num_of_chars
