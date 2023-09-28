#!/usr/bin/python3
# rectangle.py
# Travis Adamson
""" Declares a new class: Rectangle """


class Rectangle(Base):
    """Describes a new class: Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new object of Rectangle:

        Args:
            width (int): The width to set to the obj
            height (int): The height to set to the obj
            x (int): The x axis location
            y (int): The y axis location
            id (int): The id to assign to this obj
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @property
    def x(self):
        """Get the x axis location of the Rectangle"""
        return self.__x

    @property
    def y(self):
        """Get the y axis location of the Rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x axis location of Rectangle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y axis location of Rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
