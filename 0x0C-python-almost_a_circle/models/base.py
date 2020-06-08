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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of list_objs to a file
        open the file with 'with', in mode='w'

        json.dump() method can be used to write to file a JSON file directly.
        this "{}.json".format(cls.__name__) is to create a file with the name
        of each

        Function and method arguments:
        Always use 'self' for the first argument to instance methods.
        Always use 'cls' for the first argument to class methods.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w') as file:
            if list_objs is None:
                json.dump("[]", file)
            else:
                mylist_of_dict = []
                for myobject in list_objs:
                    """with to_dictiorary method, we will place each
                    value to the each key, here order matters """
                    temp_dic = cls.to_dictionary(myobject)
                    mylist_of_dict.append(temp_dic)
                "we must use the method to_json_string to pass it to string"
                json_list_dictionaries = cls.to_json_string(mylist_of_dict)
                "we must overwrite the file if it already exists"
                file.write(json_list_dictionaries)
