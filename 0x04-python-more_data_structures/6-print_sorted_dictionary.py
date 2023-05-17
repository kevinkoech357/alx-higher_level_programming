#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    after_sort = sorted(a_dictionary.keys())
    for key in after_sort:
        print(key, ':', a_dictionary[key])
