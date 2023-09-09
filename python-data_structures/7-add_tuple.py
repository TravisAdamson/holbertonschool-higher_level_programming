#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b()):
    tuple_n = (0, 0)
    if tuple_a[0] is not None:
        a = tuple_a[0]
    else:
        a = 0
    if tuple_b[0] is not None:
        b = tuple_b[0]
    else:
        b = 0
    tuple_n[0] = a + b
    if tuple_a[1] is not None:
        a = tuple_a[1]
    else:
        a = 0
    if tuple_b[1] is not None:
        b = tuple_b[1]
    else:
        b = 0
    tuple_n[1] = a + b
    return tuple_n
