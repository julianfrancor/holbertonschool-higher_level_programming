#!/usr/bin/python3

import json

"""
This class will be the “base” of all
other classes in this project
"""


class Base:
    """Summary: definning the Bass class

    Attributes:
        __nb_objects: private class attribute
        id: public instance attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initialization of the object/instance attributes
        Args:
            id(int): public, positive number
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for sharing data representation

        Static method that returns the JSON string representation
        of list_dictionaries

        json_string_representation = json.dumps(my_obj)
        where my_obj: is an object of any type to be converted to JSON

        json.dumps() method can convert a Python object into a JSON string.
        json.dump() method can be used to write to file a JSON file directly.
        can Write in an open file
        json.loads() expects to get its text from a string object
        json.load() expects to get the text from a file
        can Read from an open file an convert
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            json_string_representation = json.dumps(list_dictionaries)
            return json_string_representation
