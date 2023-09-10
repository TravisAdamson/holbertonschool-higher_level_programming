#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    high_key = ""
    high_score = 0
    for key in a_dictionary:
        value = a_dictionary.get(key)
        if value > high_score:
            high_score = value
            high_key = key
    return high_key
