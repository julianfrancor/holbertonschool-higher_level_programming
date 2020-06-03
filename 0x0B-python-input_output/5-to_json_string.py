#!/usr/bin/python3

"""function that returns the JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: object of any type to be converted to JSON
    """
    return json.dumps(my_obj)
