#!/usr/bin/python3

"""
function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    obj.__dict__ gives the dictionary description
    shows all the attributes defined for the object itself.
    """
    return(obj.__dict__)
