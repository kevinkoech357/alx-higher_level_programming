#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None:
        return None
    max = my_list[0]
    index = 0
    for index in my_list:
        if my_list[index] > my_list[0]:
            max = my_list[index]
        return max
