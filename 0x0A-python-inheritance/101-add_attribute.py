#!/usr/bin/python3

"""
function that adds a new attribute to an object if it’s possible
"""


def add_attribute(object, name="", value=""):
    """
    Args:
        name: must be a string
        attribute: must be a string
        __dict__: contains all the attributes
        which describe the object in question.
        It can be used to alter or read the attributes.
        It maps the attribute name to its value.
        setattr(): function sets the value of the attribute of an object.
        hasattr(): method returns true if an object has
        the given named attribute and false if it does not.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(object, name, value)
