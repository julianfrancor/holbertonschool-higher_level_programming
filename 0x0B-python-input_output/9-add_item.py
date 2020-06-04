#!/usr/bin/python3

"""
script that adds all arguments to a Python list, and then save them to a file

7. save_to_json_file(my_obj, filename): function that writes an Object
to a text file, using a JSON representation

8. load_from_json_file(filename): function that creates an
Object from a “JSON file”
"""

import sys
import os

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    """
    main function
    """
    filename = "add_item.json"
    "check if the file exist, if so do this..."
    if os.path.isfile(filename):
        my_obj = load_from_json_file(filename)
        "is not going to take the name of the executable"
        my_obj += sys.argv[1:]
        "save the object string in that file"
        save_to_json_file(list(my_obj), filename)
        "if the file doesn't exist, that function creates it and ave the object"
    else:
        save_to_json_file(list(sys.argv[1:]), filename)
