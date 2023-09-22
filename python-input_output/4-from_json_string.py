#!/usr/bin/python3
# 4-from_json_string.py
# Travis Adamson
""" Defines a function that returns the Python object """
import json


def from_json_string(my_str):
    """Returns the object version

    Args:
        my_str (string): The JSON string to convert
    """
    return (json.loads(my_str))
