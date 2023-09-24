#!/usr/bin/python3
# 6-load_from_json_file.py
# Travis Adamson
""" Defines a function that loads an Object from text file in JSON """
import json


def load_from_json_file(filename):
    """Loads the obj from file in json

    Args:
        filename (string): The name of file to use
    """
    with open(filename, "r") as cur_file:
        return (json.load(cur_file))
