#!/usr/bin/python3
# 10-student.py
# Travis Adamson
""" Defines a class Student"""


class Student:
    """The class for student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new object student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary rep of a student

        If attrs is a list of strings, represents only
        attributes included in that list.

        Args:
            attrs (list): (Optional) Attributes to include.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
