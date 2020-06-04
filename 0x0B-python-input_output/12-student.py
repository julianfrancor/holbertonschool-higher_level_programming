#!/usr/bin/python3

""" class Student that defines a student """


class Student:
    """docstring
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        that retrieves a dictionary representation
        of a Student instance
        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        when I type dictionary.items it will display
        a list of tuples of the content
        [(key1, value1), (key2, value2),...]
        """
        new_dict = {}
        if type(attrs) is list:
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        else:
            return(self.__dict__)
