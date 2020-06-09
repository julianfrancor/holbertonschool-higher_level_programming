#!/usr/bin/python3


""" import:
    all the modules needed (unittest and pep8)
    all the classes and methods to be tested
"""

"""
    Test suite for Almost a circle project to test:
        the methods of the Square class

    Here we have a collection of test cases, test suites or both
    All this tests should be executed together
    we create a test case based on the Class "unittest.TestCase"
"""
import unittest
import pep8
import sys
from io import StringIO
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    class to test Square Class with Unit test
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_square_instance_creation(self):
        """Test that instantiation is correct"""
        s1 = Square(5)
        self.assertIsInstance(s1, Square)
        s2 = Square(2, 2)
        self.assertIsInstance(s2, Square)

    def test_area(self):
        """Test area to display correct values"""
        s3 = Square(2, 2)
        s4 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 4)
        self.assertEqual(s4.area(), 9)
