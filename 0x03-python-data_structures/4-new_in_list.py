#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return list(my_list)
    if idx >= len(my_list):
        return list(my_list)
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
