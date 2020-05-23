#!/usr/bin/python3

"""Function that returns the sum of two intigers
"""


def add_integer(a, b=98):
    """Args:
        a (int) first argument must be integer or float
        b (int) second argument must be integer or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float('inf') or type(b) is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(a) is float('NaN') or type(b) is float('NaN'):
        raise ValueError("cannot convert float infinity to integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
