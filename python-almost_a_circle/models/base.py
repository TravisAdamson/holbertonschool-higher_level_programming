#!/usr/bin/python3
# base.py
# Travis Adamson
""" Declares a new base class """


class Base:
    """Describes a new class: Basee"""
    self.__nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new class:

        Args:
            id (int): The id to assign to this obj
        """
        if id != None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
