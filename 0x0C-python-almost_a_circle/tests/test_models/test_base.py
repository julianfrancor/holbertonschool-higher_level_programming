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
    class to test Base Class with Unit test
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_Base_instance_creation(self):
        """Test that instantiation is correct"""
        my_object = Base()
        self.assertIsInstance(my_object, Base)

    def test_not_id(self):
        """Test when not id is passed"""
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_id_is_passed(self):
        """Test when id is passed"""
        b3 = Base(7)
        self.assertEqual(b3.id, 7)

    def test_id_exists(self):
        """Test if id exists"""
        b4 = Base()
        self.assertTrue(hasattr(b4, 'id'))

    def test_base__nb_objects_exists(self):
        """Test if Base.__nb_objects class attribute exists"""
        b5 = Base()
        self.assertTrue(hasattr(b5, '_Base__nb_objects'))
