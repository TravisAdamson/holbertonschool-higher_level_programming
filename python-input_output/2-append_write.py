#!/usr/bin/python3
# 2-append_write.py
# Travis Adamson
""" Defines a function to append to a file """


def append_write(filename="", text=""):
    """Appends the given text to the given file

    Args:
        filename (file): The file to write to.
        text (string): The text to write to the file
    """
    with open(filename, "a", encoding="utf-8") as cur_file:
            return (cur_file.write(text))
