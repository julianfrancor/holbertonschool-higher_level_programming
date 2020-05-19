#!/usr/bin/python3


"""
Here we are creating a class Square that defines a square.
We are using the special method __init__ to initialize the
data attribute size, which is a private instance attribute
__size.
Also, we are rasing some exceptions in case the data "size"
that enters to initialize the object, is not intiger or is
less than cero.
"""


class Square:
    """Summary: Define a Square.

    Attributes:
        size: the size of a square
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
