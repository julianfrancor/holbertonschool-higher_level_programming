#!/usr/bin/python3
"""class LockedClass"""


class LockedClass(object):
    """docstring"""
    __slots__ = ['first_name']
    def __init__(self, first_name):
        """comments"""
        self.first_name = first_name
