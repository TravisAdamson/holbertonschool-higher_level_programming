#!/usr/bin/python3
# square.py
# Travis Adamson
""" Define a class "Square". """
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is an class to define square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square.

        Args:
            size (int): The size of the square
            x (int): The x axis value
            y (int): The y axis value
            id (int): The id of this square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self. height = value

    def __str__(self):
        """Return the rep of square for print() and str()"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
