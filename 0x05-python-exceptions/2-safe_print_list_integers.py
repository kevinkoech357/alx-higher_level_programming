#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints first x elements of my_list, only of int type.

    Args:
        my_list: list involved.
        x: number of elements.

    Return:
        Real number of integers printed.
    """
    elements = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            elements += 1

    print("")
    return (elements)
