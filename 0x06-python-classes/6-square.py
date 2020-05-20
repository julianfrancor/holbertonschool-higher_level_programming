#!/usr/bin/python3


"""
Here we are creating a class Square that defines a square.
We are using the special method __init__ to initialize the
data attribute size, which is a private instance attribute
__size.
we are rasing some exceptions in case the data "size"
that enters to initialize the object, is not intiger or is
less than cero.
we are defining a method to calculate the area of the square
we are using @property and @size.setter
we are creating a method to print square
"""


class Square:
    """Summary: Define a Square.

    Attributes:
        size: private instance attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the instance attributes
            Args:
            size(int): private, zero or positive number
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates the area of a square
            Return: the square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """method which is used for getting
            a value is decorated with "@property"
            (also known as 'accessor')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Return: the data value
        """
        return self.__size

    @size.setter
    def size(self, value):
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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """method which is used for getting
            a value is decorated with "@property"
            (also known as 'accessor')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Return: the data value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """method which has to function as the setter is to change
            the value and is decorated with "@position.setter"
            (also know as 'mutator')
            These methods are of course the getter for retrieving the data
            and the setter for changing the data. According to this principle,
            the attributes of a class are made private to hide and protect them
            from other code.
            Changes the data
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = position
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints in stdout the square with the character '#'
        """
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print()
        for j in range(0, self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
