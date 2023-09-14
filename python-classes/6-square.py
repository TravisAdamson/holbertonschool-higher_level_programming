#!/usr/bin/python3
# 3-square.py
# Travis Adamson
""" Define a class "Square". """


class Square:
    """This is an empty class to define square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new "Square".

        Args:
            size (int): The size of said new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size of Square

        Args:
            self (square): The square to get the size of
        """
        return (self.__size)

    @property
    def position(self):
        """Retrieves the position of square

        Args:
            self (square): The square to get the position of.
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """Sets the size value of the Square

        Args:
            self (square): The given Square
            value (int): The size of to set to Square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            self (square): The given square.
            value (tuple): The position to set
        """
        err_msg = "position must be a tuple of 2 positive integers"
        if len(value) != 2:
            raise TypeError(err_msg)
        if not isinstance(value, tuple):
            raise TypeError(err_msg)
        if not all(isinstance(val, int) for val in value):
            raise TypeError(err_msg)
        if not all(val >= 0 for val in value):
            raise TypeError(err_msg)
        self.__position = value

    def area(self):
        """Calculates the area of the given square

        Args:
            self (square): THe square to calculate with.        """
        return (self.__size * self.__size)

    def my_print(self):
        """ prints the square using #

        Args:
            self (square): The square to rpint
        """
        if self.__size > 0:
            if self.__position[0] > 0:
                for i in range(self.__size):
                    for sp in range(self.__position[0]):
                        print(" ", end="")
                    for j in range(self.__size):
                        print("#", end="")
                    print()
            else:
                for i in range(self.__size):
                    for j in range(self.__size):
                        print("#", end="")
                    print()
        else:
            print()
