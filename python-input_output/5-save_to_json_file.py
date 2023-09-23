#!/usr/bin/python3
# 5-save_to_json_file.py
# Travis Adamson
""" Defines a function that writes an Object to text file in JSON """
import json


def save_to_json_file(my_obj, filename):
    """Writes the obj to file in json

    Args:
        my_obj (object): The Object to convert
        filename (string): The name of file to use
    """
    json_string = json.dumps(my_obj)
    with open(filename, "w") as cur_file:
        cur_file.write(json_string)
