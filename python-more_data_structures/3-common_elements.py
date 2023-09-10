#!/usr/bin/python3

def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return 0
    new_set = set()
    for i in set_1:
        if i in set_2:
            new_set.add(i)
    return new_set
