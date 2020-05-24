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
    for c in range(0, len(text)):
        print(text[c], end='')
        if text[c] in delimiters:
            print("\n\n")
            if text[c + 1] == " ":
                c += 1
        c += 1
