#!/usr/bin/python3

import unittest
import pep8
from models.base import Base
""" import:
    all the modules needed (unittest and pep8)
    all the classes and methods to be tested
"""

"""
    Test suite for Almost a circle project to test:
        the methods of the Base class

    Here we have a collection of test cases, test suites or both
    All this tests should be executed together
    we create a test case based on the Class "unittest.TestCase"
"""


class TestBase(unittest.TestCase):
    """
    class to test  Base Class
    with Unit test
    """

    def test_right_output(self):
        '''
        Testing the right output
        '''
        