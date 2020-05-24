#!/usr/bin/python3

"function that prints a square with the character"


def text_indentation(text):
    """Args:
        text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimiters = [".", "?", ":"]
    temp = 0
    for i, c in enumerate(text):
        if c in delimiters:
            print(text[temp: i + 1].strip(), end="\n\n")
            temp = i + 1
        elif i == len(text) - 1:
            print(text[temp: i + 1].strip(), end="")
