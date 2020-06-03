#!/usr/bin/python3

"""
function that reads a text file (UTF8) and prints it to stdout
"""


def write_file(filename="", text=""):
    """
    Args:
        filename
        text: to be added in the file
    """
    with open(filename, mode='w', encoding="UTF8") as file:
        return file.write(text)
