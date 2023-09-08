#!/usr/bin/python3

def no_c(my_string):
    new_i = 0
    if my_string is not None:
        for i in range(0, len(my_string) - 1):
            if ord(my_string[i]) != 67 and ord(my_string[i]) != 99:
                new_my_string[new_i] = my_string[i]
                new_i += 1
