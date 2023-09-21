#!/usr/bin/python3
# 2-is_same_class.py
# Travis Adamson
""" Defines a function to determine if obj matches the class """


def is_same_class(obj, a_class):
    """Determines if obj is exactly of class a_class

    Args:
        obj (any): The given object to check
        a_class (any): The class to compare to

    Returns: True if exactly matches otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
