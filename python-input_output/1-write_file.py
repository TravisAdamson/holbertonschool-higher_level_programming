#!/usr/bin/python3
# 1-write_file.py
# Travis Adamson
""" Defines a function to write to a file """


def write_file(filename="", text=""):
    """Writes the given text to the given file

    Args:
        filename (file): The file to write to.
        text (string): The text to write to the file
    """
    with open(filename, "w", encoding="utf-8") as cur_file:
            cur_file.write(text)
