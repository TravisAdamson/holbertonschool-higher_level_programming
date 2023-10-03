#!/usr/bin/python3
import json
"""Base class module"""


class Base:
    """Base class repr"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string represenation through serialization"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json string representation to file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            json_string = [obj.to_dictionary() for obj in list_objs]
            f.write(Base.to_json_string(json_string))

    @staticmethod
    def from_json_string(json_string):
        """Returns an object from the json string provided

        Args:
            json_string (str): A Json string of a list of dictionaries
        Returns:
            Empty list or object represented by the string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instace with all attributes set"""
        if dictionary:
            if cls.__name__ == "Rectangle":
                instance = cls(3, 3)
            else:
                instance = cls(3)
            instance.update(**dictionary)
            return instance

    def load_from_file(cls):
        """Returns a list of classes created from json strings

        Reads from <cls.__name__>.json

        Returns:
            Empty list or a list of created classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                list_dictionaries = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dictionaries]
        except IOError:
            return []
