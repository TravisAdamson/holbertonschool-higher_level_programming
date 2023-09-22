#!/usr/bin/python3
# 9-rectangle.py
# Travis Adamson
""" Define a class "Rectangle" using "BaseGeometry". """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class Rectangle that inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initializes an object of Rectangle

        Args:
            width (int): The width of the object
            height (int): The height of the object
        Validates both width and height using integer validator
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __repr__(self):
        """Returns the string presentation of Rectangle"""
        str_rectangle = "[Rectangle] " + str(self.__width)
        str_rectangle += "/" + str(self.__height)
        return str_rectangle

    def __str__(self):
        """Returns the printable version of the object"""
        str_rectangle = "[Rectangle] " + str(self.__width)
        str_rectangle += "/" + str(self.__height) 
        return str_rectangleuuu
