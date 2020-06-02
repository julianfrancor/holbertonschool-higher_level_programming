#!/usr/bin/python3

"""class Square that inherits from Rectangle (9-rectangle.py):"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """docstring"""

    def __init__(self, size):
        """
        size must be a positive integer,
        validated by integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of the rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """method to print a string"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
