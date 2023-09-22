#!/usr/bin/python3
# 11.square.py
# Travis Adamson
""" Define a class "Rectangle" using "BaseGeometry". """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square that inherits Rectangle"""

    def __init__(self, size):
        """Initializes an object of Square

        Args:
            size (int): The size of the object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
