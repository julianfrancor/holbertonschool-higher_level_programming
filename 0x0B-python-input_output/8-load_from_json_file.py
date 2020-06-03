#!/usr/bin/python3

"""
function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    Args
        filename: JSON file form where the string
        is going to be read

    json.dumps() method can convert a Python object into a JSON string.
    json.dump() method can be used to write to file a JSON file directly.
    can Write in an open file

    json.loads() expects to get its text from a string object
    json.load() expects to get the text from a file
    can Read from an open file an convert

    """
    with open(filename, mode="r", encoding="UTF8") as file:
        return json.load(file)
