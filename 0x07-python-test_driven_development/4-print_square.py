#!/usr/bin/python3

""" function that prints a square with the character #
"""


def print_square(size):
    """ function that prints a square with the character #

    Args:
            size must be an integer and is the size length of the square

    Raise error exceptions:
            TypeError: size must be an integer
            ValueError: size must be >= 0
            TypeError: size must be an integer
    Returns:
            No return value
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
