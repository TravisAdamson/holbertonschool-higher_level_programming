#!/usr/bin/python3
# 0-square.py
# Travis Adamson
""" Define a class "BaseGeometry". """


class BaseGeometry:
    """This is an empty class to define BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        te_msg = name + " must be an integer"
        ve_msg = name + " must be greater than 0"
        if type(value) is not int:
            raise TypeError(te_msg)
        if value <= 0:
            raise ValueError(ve_msg)
