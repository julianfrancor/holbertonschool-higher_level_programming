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
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] in delimiters:
            print()
            print()
            if text[i + 1] == " ":
                i += 1
            i += 1
