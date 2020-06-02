#!/usr/bin/python3

"""class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """
        we have to override __init__.
        Overriding is altering or replacing a method
        of the superclass with a new method (with the same name)
        in the subclass.
        Any method can be overridden, not just __init__.

        SUPER function is a way to call code on the parent class.
        it returns the object as an instance of the parent class,
        allowing us to call the parent method directly
        """
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """method to print a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
