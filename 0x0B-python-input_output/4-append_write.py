#!/usr/bin/python3

"""
function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Args:
        filename
        text: to be added at the end of the file
    """
    with open(filename, mode='a', encoding="UTF8") as file:
        return file.write(text)
