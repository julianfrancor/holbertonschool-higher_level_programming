#!/usr/bin/python3

""" function that prints a square with the character #
"""


def text_indentation(text):
    """ function that prints a square with the character #

    Args:
            text must be a string

    Raise error exceptions:
            TypeError: text must be a string

    Returns:
            No return value
    """
    delimiters = [".", "?", ":"]
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = 0
    for i, c in enumerate(text):
        if c in delimiters:
            print(text[temp: i + 1], end="\n\n")
            temp = i + 1
        elif i == len(text) - 1:
            print(text[temp: i + 1].strip(), end="")
