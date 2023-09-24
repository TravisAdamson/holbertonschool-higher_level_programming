#!/usr/bin/python3
# 8-class_to_json.py
# Travis Adamson
""" Defines a function to convert class to JSON"""


def class_to_json(obj):
    """Returns the dictionary rep of a simple structure"""
    return obj.__dict__
