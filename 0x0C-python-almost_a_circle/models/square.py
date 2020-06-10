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
        Calling the super class with 'width' and 'height' as 'size', 'x',
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
        """Here we are calling the method from the superclass
        super().__setattr__('width', value)
        super().__setattr__('height', value)"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overwriting the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute with args or kwargs
        (kwargs: key-worded argument that is like a dictionary key/value)
        here we use super().__setattr__(...) to call the method from the
        superclass
        """
        if args is None or not args:
            for key, value in kwargs.items():
                super.__setattr__(self, key, value)
        else:
            args_updated = ['id', 'size', 'x', 'y']
            for index, value in enumerate(args):
                super.__setattr__(self, args_updated[index], value)

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation of a Square
        """
        dic_square = {'id': self.id, 'size': self.size,
                      'x': self.x, 'y': self.y}
        return dic_square
