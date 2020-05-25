#!/usr/bin/python3


"""class Rectangle that defines a rectangle and define
the methods getter and setter for the attributes width and height
Adding method __str__ to print the rectangle
"""


class Rectangle:
    """Define a Rectangle.

    Attributes:
        width: private instance attribute
        height: private instance attribute

    """

    def __init__(self, width=0, height=0):
        """Initialization of the instance attributes
            Args:
            width(int): private, zero or positive number
            height(int): private, zero or positive number
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
        return self.__height

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

    def area(self):
        """Calculates the area of a rectangle
            Return: the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle
            Return: the rectangle perimiter
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Method to print a attribute
        """
        string = ""
        if (self.__width == 0) or (self.__height == 0):
            return string
        for i in range(self.__height - 1):
            string += (("#" * self.__width) + "\n")
        string += (("#" * self.__width))
        return string
