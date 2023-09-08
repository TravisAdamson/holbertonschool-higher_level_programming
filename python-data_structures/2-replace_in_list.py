#!/usr/bin/python3

def replace_in_list((my_list, idx, element):
    if idx < 0:
        return my_list
    if my_list is not None and type(my_list) == list:
        if len(my_list) <= idx:
            return my_list
        my_list[idx] = element
    return my_list
