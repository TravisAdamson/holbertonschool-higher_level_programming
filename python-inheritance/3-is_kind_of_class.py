#!/usr/bin/python3
# 2-is_kind_of_class.py
# Travis Adamson
""" Defines a function to determine if obj matches the class """


def is_same_class(obj, a_class):
    """Determines if obj is of class a_class (exactly or inherited)

    Args:
        obj (any): The given object to check
        a_class (any): The class to compare to

    Returns: True if matches otherwise False
    """
    if type(obj) == a_class:
        return True
    elif type(type(obj)) == a_class:
        return True
    else:
        return False
