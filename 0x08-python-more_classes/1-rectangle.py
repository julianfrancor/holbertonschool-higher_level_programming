#!/usr/bin/python3


"Empty class Rectangle that defines a rectangle"


class Rectangle:
    """Define a Rectangle.

    Attributes:
        width: private instance attribute
        height: private instance attribute

    """

    def __init__(self, width=0, height=0):
        """Initialization of the instance attributes
            Args:
            size(int): private, zero or positive number
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method which is used for getting
            a value is decorated with "@property"
            (also known as 'accessor')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Return: the data value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """method which has to function as the setter is to change
            the value and is decorated with "@methodname.setter"
            (also know as 'mutator')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Changes the data
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method which is used for getting
            a value is decorated with "@property"
            (also known as 'accessor')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Return: the data value
        """
        return self.__width

    @height.setter
    def height(self, value):
        """method which has to function as the setter is to change
            the value and is decorated with "@methodname.setter"
            (also know as 'mutator')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Changes the data
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
