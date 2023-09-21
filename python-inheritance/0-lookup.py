#!/usr/bin/python3
# 0-lookup.py
# Travis Adamson
""" Defines a function to get all attributes and methods of an ojbect """


def lookup(obj):
    """Returns the a list with attributes and methods of ojb.

    Args:
        obj (any): The object to get the list from
    """
    return (list(dir(obj)))
