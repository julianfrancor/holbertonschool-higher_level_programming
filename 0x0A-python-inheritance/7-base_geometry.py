#!/usr/bin/python3

"""class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry():
    """docstring"""

    def area(self):
        """that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
