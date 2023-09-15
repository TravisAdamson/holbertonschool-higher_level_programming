#!/usr/bin/python3
# 0-add_integer.py
# Travis Adamson
""" Defines a function to add two integers """


def add_integer(a, b=98):
    """Returns the result of adding integers a and b.

    Float arguments will be typecasted to int before adding.

    Raises:
        TypeError: if a or b are not float or int
    """
    te_msg_a = "a must be an integer"
    te_msg_b = "b must be an integer"
    oe_msg = "cannot convert float infinity to integer"
    ve_msg = "cannot convert float NaN to integer"
    if type(a) != int and type(a) != float:
        raise TypeError(te_msg_a)
    if type(b) != int and type(b) != float:
        raise TypeError(te_msg_b)
    return int(a) + int(b)
