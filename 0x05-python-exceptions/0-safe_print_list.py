#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of my_list.

    Args:
        my_list: list involved
        x: number of elements to be printed

    Return:
        Number of elements printed.
    """
    element_number = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            element_number += 1
        except IndexError:
            break
    print("")
    return (element_number)
