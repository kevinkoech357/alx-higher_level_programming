#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    else:
        new_list = []
        for index in my_list:
            if index % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
