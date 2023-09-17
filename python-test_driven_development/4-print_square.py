#!/usr/bin/python3
# 4-print_square.py
# Travis Adamson
""" Defines a function that prints a squre using # """


def print_square(size):
    """Prints a square using #

    Size is the number of rows and collumns.

    Raises:
        TypeError: if values are not ints great than 0
        ValueError: if size is not >= 0
    """
    te_msg = "size must be an integer"
    ve_msg = "size must be >= 0"
    if type(size) != int:
        raise TypeError(te_msg)
    if size < 0:
        raise ValueError(ve_msg)
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
