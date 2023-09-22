#!/usr/bin/python3
# 4-inherits_from.py
# Travis Adamson
""" Defines a function to determine if obj inherited the given class """


def inherits_from(obj, a_class):
    """Determines if obj inherits from a_class

    Args:
        obj (any): The given object to check
        a_class (any): The class to compare to

    Returns: True if inherits otherwise False
    """
    if isinstance(obj, a_class):
        return True
    if issubclass(obj.__class__, a_class):
        return True
    else:
        return False
