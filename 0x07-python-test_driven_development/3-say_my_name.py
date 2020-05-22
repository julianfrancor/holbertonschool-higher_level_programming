#!/usr/bin/python3

"""function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>

    Args:
            first_name (str) must be strings
            last_name (str) must be strings

    Raise error exceptions:
            TypeError: first_name must be a string
            TypeError: last_name must be a string

    Returns:
            Returns a new matrix
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
