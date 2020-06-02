#!/usr/bin/python3

"""
function that returns True if the object
is exactly an instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Here I have to use type instead of isinstance()
    because in the task anouncement they are asking me if
    the object is 'EXACTLY' an instance if a specified class
    or not.
    """
    if type(obj) is a_class:
        return True
    return False
