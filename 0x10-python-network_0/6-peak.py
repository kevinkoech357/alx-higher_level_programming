#!/usr/bin/python3

"""
This module contains a method
that finds the peak in a list
of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(list): unsorted list of int

    Return:
        peak
    """
    # Check if param is a list
    if type(list_of_integers) != list:
        return
    # Check if param is empty
    if not list_of_integers:
        return None


    left = 0
    right = len(list_of_integers) - 1

    # Loop through the list
    while left < right:
        # Find the int at the center, ignore float
        mid = (left + right) // 2
        # Compare surrounding int values
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
