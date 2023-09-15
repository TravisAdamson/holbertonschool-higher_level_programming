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
    te_msg_a = "TypeError: a must be an integer"
    te_msg_b = "TypeError: b must be an integer"
    oe_msg = "OverflowError: cannot convert float infinity to integer"
    ve_msg = "ValueError: cannot convert float NaN to integer"
    if type(a) == float:
        try:
            a = int(a)
        except OverflowError as oe:
            print(oe_msg)
            return None
        except ValueError as ve:
            print(ve_msg)
            return None
    if type(b) == float:
        try:
            b = int(b)
        except OverflowError as oe:
            print(oe_msg)
            return None
        except ValueError as ve:
            print(ve_msg)
            return None
    if type(a) != int:
        try:
            raise TypeError
        except TypeError as te:
            print(te_msg_a)
            return None
    if type(b) != int:
        try:
            raise TypeError
        except TypeError as te:
            print(te_msg_b)
            return
    return a + b
