#!/usr/bin/python3

"""
Creates a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class MyList that inherits from list.
    """
    def print_sorted(self):
        """
        A public instance method that prints the
        list in ascending order.

        Assumptions:
            Elements in the list are of int type.
        """
        sorted_list = sorted(self)
        print(sorted_list)
