#!/usr/bin/python3

"""class MyInt that inherits from int"""


class MyInt(int):
    """docstring"""

    def __init__(self, value):
        """value is any intiger passed
        """
        self.__value = value

    def __eq__(self, other):
        """
        Object Equality method (inverted with the Inequality)
        Normally it should be '==' but it has "not" at the begining
        """
        return not self.__value == other

    def __ne__(self, other):
        """
        Object Inequality method (inverted with the Equality)
        Normally it should be '!=' but it has "not" at the begining
        """
        return not self.__value != other

    def __str__(self):
        """method to print a string"""
        return "{}".format(self.__value)
