#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if not a_dictionary:
        return None
    top_key = max(a_dictionary, key=a_dictionary.get)
    top_score = a_dictionary[top_key]

    return top_key
