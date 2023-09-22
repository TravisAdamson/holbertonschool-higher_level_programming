#!/usr/bin/python3
# 0-square.py
# Travis Adamson
""" Define a class "BaseGeometry". """


class BaseGeometry:
    """This is an empty class to define BaseGeometry"""

    def area(self):
        """ Not impletemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer

        Args:
            name (str): The name of the parameter
            value (int): The value to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0.
        """
        te_msg = name + " must be an integer"
        ve_msg = name + " must be greater than 0"
        if type(value) != int:
            raise TypeError(te_msg)
        if value <= 0:
            raise ValueError(ve_msg)
