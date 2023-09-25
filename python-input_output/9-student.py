#!/usr/bin/python3
# 8-class_to_json.py
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

    def to_json(self):
        """Returns the dictionary rep of a student"""
        return self.__dict__
