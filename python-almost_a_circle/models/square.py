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
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square:

        Args:
            *args (ints): New attribute values.
                - 1st argument is id attribute
                - 2nd argument is size attribute
                - 3rd argument is x attribute
                - 4th argument is y attribute
            **kwargs (dict): New pairs of atributes using key/value
        """
        if args and len(args) != 0:
            count = 0
            for argument in args:
                if count == 0:
                    if argument is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = argument
                elif count == 1:
                    self.size = argument
                elif count == 2:
                    self.x = argument
                elif count == 3:
                    self.y = argument
                count += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary rep of Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the rep of square for print() and str()"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
