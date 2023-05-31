#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides 2 integers an prints the result.

    Args:
        a: first integer.
        b: second integer.

    Return:
        Result of a / b.
    """

    try:
        result = a / b
    except TypeError:
        result = None
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
