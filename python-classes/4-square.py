#!/usr/bin/python3
# 3-square.py
# Travis Adamson
""" Define a class "Square". """


class Square:
    """This is an empty class to define square"""

    def __init__(self, size=0):
        """Initializes a new "Square".

        Args:
            size (int): The size of said new square.
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of the given square

        Args:
            self (square): THe square to calculate with.
        """
        return (self.__size * self.__size)

    def size(self):
        """Retrieves the size of Square

        Args:
            self (square): The square to get the size of
        """
        return self.__size

    def size(self, value):
        """Sets the size value of the Square

        Args:
            self (square): The given Square
            value (int): The size of to set to Square.
        """
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
