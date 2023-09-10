#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_sorted_keys = sorted(dict.items(), key=lambda x: x[0])
    for key, value in my_sorted_keys:
        print("{:s}: {}".format(key, value))
