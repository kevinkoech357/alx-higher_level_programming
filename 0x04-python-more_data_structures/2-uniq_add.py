#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None:
        return None
    list_values = set()
    sum_of_unique = 0
    for index in my_list:
        if index not in list_values:
            sum_of_unique += index
            list_values.add(index)
    return sum_of_unique
