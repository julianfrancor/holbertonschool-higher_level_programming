#!/usr/bin/python3

"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
"""

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

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """method to print a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
