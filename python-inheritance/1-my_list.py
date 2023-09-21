#!/usr/bin/python3
# 1-my_list.py
# Travis Adamson
""" Defines an inherited list class MyList """


class MyList(list):
    """implements a sorted print for list class"""

    def print_sorted(self):
        """Prints the given list in ascending order"""
        print(sorted(self))
