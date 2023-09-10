#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return 0
    new_set = set()
    for i in set_1:
        if i not in set_2:
            new_set.add(i)
    for i in set_2:
        if i not in set_1:
            new_set.add(i)
    return new_set
