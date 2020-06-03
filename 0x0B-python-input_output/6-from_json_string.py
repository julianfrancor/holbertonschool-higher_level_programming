#!/usr/bin/python3

"""function that returns the JSON representation of an object (string)"""

import json


def from_json_string(my_str):
    """
    Args:
        my_obj: object of any type to be converted to JSON
    """
    return json.loads(my_str)
