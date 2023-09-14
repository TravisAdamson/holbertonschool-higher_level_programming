#!/usr/bin/python3
# 0-square.py
# Travis Adamson
""" Define a class "Square". """


class Square:
    """This is an empty class to define square"""

    def __init__(self, size=0):
        """Initializes a new "Square".

        Args:
            size (int): The size of said new square.
        """
        if type(size) != int:
            try:
                raise TypeError
            except TypeError as te:
                print("size must be an integer")
        if size < 0:
            try:
                raise ValueError
            except ValueError as ve:
                print("size must be >= 0")
        size.__size = size
