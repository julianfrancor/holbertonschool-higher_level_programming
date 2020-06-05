#!/usr/bin/python3

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
