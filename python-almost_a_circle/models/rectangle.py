#!/usr/bin/python3
# rectangle.py
# Travis Adamson
""" Declares a new class: Rectangle """
from models.base import Base


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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x axis location of Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y axis location of Rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Print rectangle represented by # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle:

        Args:
            *args (ints): New attribute values.
                - 1st argument is id attribute
                - 2nd argument is width attribute
                - 3rd argument is height attribute
                - 4th argument is x attribute
                - 5th argument is y attribute
            **kwargs (dict): New pairs of atributes using key/value
        """
        if args and len(args) != 0:
            count = 0
            for argument in args:
                if count == 0:
                    if argument is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argument
                elif count == 1:
                    self.width = argument
                elif count == 2:
                    self.height = argument
                elif count == 3:
                    self.x = argument
                elif count == 4:
                    self.y = argument
                count += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary rep of the Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns the print() and str() rep of rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))
