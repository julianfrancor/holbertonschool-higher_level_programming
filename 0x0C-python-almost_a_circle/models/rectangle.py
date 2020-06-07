#!/usr/bin/python3

"""
class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Summary: definning the class Rectangle that inherits from Base

    Attributes:
        Private instance attributes
        __width -> width
        __height -> height
        __x -> x
        __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of the object/instance attributes
        Args:
            __width: width
            __height -> height
            __x -> x
            __y -> y
        Calling the super class with 'id' - this super() call
        with use of the logic of the __init__ of the Base class
        will help us to extend the functinality of the inherited method
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the with of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Gets the with of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Gets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the intercept with the x-axis of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the intercept with the x-axis of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the intercept with the y-axis of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the intercept with the y-axis of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character '#'"""
        string = ""
        string = "\n" * self.y
        for i in range(self.height - 1):
            string += (" " * self.x + ("#" * self.width) + "\n")
        string += (" " * self.x + ("#" * self.width))
        print(string)

    def __str__(self):
        """overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
        self.x, self.y, self.width, self.height)
