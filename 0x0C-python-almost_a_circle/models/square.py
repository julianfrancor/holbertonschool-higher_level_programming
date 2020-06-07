#!/usr/bin/python3

"""
class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Summary: definning the class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of the object/instance attributes
        Args:
            size
            x
            y
            id
        Calling the super class with 'width' and 'height' as size', 'x',
        'y' and 'id' this super() call with use of the logic of the __init__
        of the Base class. super() will help us to extend the functinality
        of the inherited method
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        "Getter that retrieves the size value of the square"
        return self.width

    @size.setter
    def size(self, value):
        """Here we are calling the method from the superclass"""
        super().__setattr__('width', value)
        super().__setattr__('height', value)


    def __str__(self):
        """Overwriting the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width)
