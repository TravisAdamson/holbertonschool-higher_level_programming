#!/usr/bin/python3

def no_c(my_string):
    new_i = 0
    new_my_string = ""
    if my_string is not None:
        for i in range(0, len(my_string)):
            if my_string[i] != "c" and my_string[i] != "C":
                new_my_string += my_string[i]
    return new_my_string
