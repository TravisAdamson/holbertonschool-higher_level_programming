#!/usr/bin/python3
# 1-my_list.py
# Travis Adamson
""" Defines a class MyList that inherits from list """


class MyList(list):
    """Adds sorted printing for existing class: list"""

    def print_sorted(self):
        """Prints the given list in ascending order"""
        print(sorted(self))
