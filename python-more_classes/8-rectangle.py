#!/usr/bin/python3
# 8-rectangle.py
# Travis Adamson
""" Define a class "Rectangle". """


class Rectangle:
    """This is a class to define Rectangle.

    Attributes:
        number_of_instances (int): How many rectangles exist.
        print_symbol (any): The symbol used to represent as a string.
    """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Intializes a new "Rectangle".

        Args:
            self (Rectangle): The Rectangle
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle

        Args:
            self (Rectangle): The Rectangle of to get the width of.
        """
        return (self.__width)

    @property
    def height(self):
        """Retrieves the height of the Rectangle.

        Args:
            self (Rectangle): The Rectangle to get the height of.
        """
        return (self.__height)

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle

        Args:
            self (Rectangle): The given Rectangle
            value (int): The width to set to Rectangle
        """
        ve_msg_w = "width must be >= 0"
        te_msg_w = "width must be an integer"
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError(ve_msg_w)
        else:
            raise TypeError(te_msg_w)

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle

        Args:
            self (Rectangle): The given Rectangle
            value (int): The height to set to Rectangle
        """
        te_msg_h = "height must be an integer"
        ve_msg_h = "height must be >= 0"
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError(ve_msg_h)
        else:
            raise TypeError(te_msg_h)

    def area(self):
        """Calculates the area of the given Rectangle

        Args:
            self (Rectangle): The given Rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the given Rectangle

        Args:
            self (Rectangle): The given Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def bigger_or_equal(rect_1, rect_2):
        """Finds the bigger rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return(rect_2)

    def __str__(self):
        """Return the printable version of the Rectangle.

        Represents the rectangle with #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_like = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_like.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectangle_like.append("\n")
        return ("".join(rectangle_like))

    def __repr__(self):
        """Returns the string representation of the Rectangle."""
        str_rectangle = "Rectangle(" + str(self.__width)
        str_rectangle += ", " + str(self.__height) + ")"
        return str_rectangle

    def __del__(self):
        """Detects any Rectangle being deleted and prints a message"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
