#!/usr/bin/python3

"""class BaseGeometry (based on 5-base_geometry.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """docstring"""

    def __init__(self, width, height):
        """
        width and height must be positive integers,
        validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
