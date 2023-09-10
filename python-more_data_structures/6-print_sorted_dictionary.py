#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_sorted_keys = sorted(dict.items(), key=lamda x: x[0])
    for key_pairs in my_sorted_keys:
        print(key_pairs)
