#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    new_value = 0
    new_dictionary = {}
    for key, value in a_dictionary:
        new_value = value * 2
        new_dictionary[key] = new_value
    return new_dictionary
