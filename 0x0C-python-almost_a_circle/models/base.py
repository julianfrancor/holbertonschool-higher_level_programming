#!/usr/bin/python3


"""
This class will be the “base” of all
other classes in this project
"""
import json


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
        static method that returns the JSON string representation
        of list_dictionaries. (JSON is one of the standard formats
        for sharing data representation)

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
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of list_objs to a file
        open the file with 'with', in mode='w'

        json.dump() method can be used to write to file a JSON file directly.
        this "{}.json".format(cls.__name__) is to create a file with the name
        of each class

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
                    value to each key, here order matters """
                    temp_dic = cls.to_dictionary(myobject)
                    mylist_of_dict.append(temp_dic)
                "we must use the method to_json_string to pass it to string"
                json_list_dictionaries = cls.to_json_string(mylist_of_dict)
                "we must overwrite the file if it already exists"
                file.write(json_list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string
        json.loads() expects to get its text from a string object
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all attributes already set
        “dummy” is an instance
        """
        if cls.__name__ == "Rectangle":
            """ Here we are instantiating with 2 arguments because we instantiate
            from class rectangle like this Rectangle(width, height) """
            dummy = cls(3, 5)
        elif cls.__name__ == "Square":
            """ Here we are instantiating with 2 arguments because we instantiate
            from class square like this Square(size) """
            dummy = cls(4)
            """here we are creating a new instance with new arguments"""
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        class method def load_from_file(cls): that returns a list of instances
        json.load() gets the text from a file and convert it to object
        """
        filename = "{}.json".format(cls.__name__)
        if not filename:
            return []
        else:
            with open(filename, mode='r') as file:
                "here we read the file and return not a string but a object"
                dict_json = file.read()
                "convert from object to json string respresentation of a dic"
                string_json = cls.from_json_string(dict_json)
                list_json = []
                for element_kwarg in string_json:
                    """create an object but we update the elements
                    we are sending a **kwarg and appending it to a list """
                    temp = cls.create(**element_kwarg)
                    list_json.append(temp)
                return list_json
