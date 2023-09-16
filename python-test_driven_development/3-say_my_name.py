#!/usr/bin/python3
# 3-say_my_name.py
# Travis Adamson
""" Defines a function that prints first and last name """


def say_my_name(first_name, last_name=""):
    """Prints the given first and last name..

    Both arguments must be strings.

    Raises:
        TypeError: if values are not strings
    """
    te_msg_a = "first_name must be a string"
    te_msg_b = "last_name must be a string"
    if type(first_name) != str:
        raise TypeError(te_msg_a)
    if type(last_name) != str:
        raise TypeError(te_msg_b)
    pr_msg = "My name is " + first_name + " " + last_name
    print(pr_msg)
