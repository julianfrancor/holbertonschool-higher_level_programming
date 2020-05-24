#!/usr/bin/python3

"function that prints a square with the character"


def text_indentation(text):
    """Args:
        text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimiters = [".", "?", ":"]
    aux = "."
    for char in text:
        if char is " " and aux in delimiters:
            continue
        print(char, end="")
        if char in delimiters:
            print("\n")
        aux = char
