#!/usr/bin/python3
# 3-to_json_string.py
# Travis Adamson
""" Defines a function that returns the JSON representation """
import json

def to_json_string(my_obj):
    """Returns the objects JSON representation

    Args:
        my_obj (object): The object to represent
    """
    return (json.dumps(my_obj))
