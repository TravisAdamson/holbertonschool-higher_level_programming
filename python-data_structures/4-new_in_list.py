#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is not None and type(my_list) == list:
        new_my_list = my_list.copy()
        if idx < 0:
            return new_my_list
        if idx > len(my_list):
            return new_my_list
        new_my_list[idx] = element
        return new_my_list
