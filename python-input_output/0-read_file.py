#!/usr/bin/python3
# 0-read_file.py
# Travis Adamson
""" Defines a function to read and print a file """


def read_file(filename=""):
    """Prints the contents of the given file.

    Args:
        filename (file): The file to read and print.
    """
    with open(filename, "r") as cur_file:
        content = cur_file.read()
        print(content)
