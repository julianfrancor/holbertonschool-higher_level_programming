#!/usr/bin/python3

"""function that writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Args
        my_obj: object of any type to be converted to JSON
        filename: filename where the string representation
        is going to be written

    json.dumps() method can convert a Python object into a JSON string.
    json.dump() method can be used for writing to JSON file.
    """
    with open(filename, mode='w', encoding="UTF8") as file:
        json.dump(my_obj, file)
