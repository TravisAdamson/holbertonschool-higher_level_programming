#!/usr/bin/python3

def max_integer(my_list=[]):
    max_i = 0
    if my_list:
        max_i = my_list[0]
        for i in range(0, len(my_list)):
            if my_list[i] > max_i:
                max_i = my_list[i]
        return max_i
    else:
        return None
