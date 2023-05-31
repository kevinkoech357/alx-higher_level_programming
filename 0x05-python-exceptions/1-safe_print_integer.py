#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer with "{.d}".format()

    Args:
        Value: Integer to be printed.

    Return:
        True if value is correctly printed.
        Otherwise - False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
