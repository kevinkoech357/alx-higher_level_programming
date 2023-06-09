#!/usr/bin/python3

"""
This module contains a function that performs text
indentation when it encounters these characters: . ? :
"""


def text_indentation(text):
    """
    Performs text indentation.

    Args:
        text: Text involved
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        chars_involved = ['.', '?', ':']
        output = ""
        for char in text:
            output += char
            if char in chars_involved:
                output += "\n\n"
        print(output.strip())
