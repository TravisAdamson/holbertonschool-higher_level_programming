#!/usr/bin/python3
# 9-rectangle.py
# Travis Adamson
""" Define a class "Rectangle" using "BaseGeometry". """
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Initializes an object of Rectangle

        Args:
            size (int): The size of the object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
