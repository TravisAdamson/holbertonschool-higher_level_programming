#!/usr/bin/python3
# 5-text_indentation.py
# Travis Adamson
""" Defines a function that inserts 2 new lines after specific characters """


def text_indentation(text):
    """Inserts 2 new lines at "." "?" and ":" characters.

    Text is the given text to print.

    Raises:
        TypeError: if text is not a string value
    """
    te_msg = "text must be a string"
    if type(text) != str:
        raise TypeError(te_msg)
    if text == None:
        raise TypeError(te_msg)
    flag = 0
    for i in text:
        if i != " " or flag == 1:
            if i != ":" and i != "?" and i != ".":
                print(i, end="")
                if i != "\n":
                    flag = 1
            else:
                print(i)
                print()
                flag = 0
