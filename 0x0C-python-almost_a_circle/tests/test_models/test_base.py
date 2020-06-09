#!/usr/bin/python3


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
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string(self):
        """Test method works well"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

        empty_dictionary = Base.to_json_string([])
        self.assertIsInstance(empty_dictionary, str)
        self.assertEqual(empty_dictionary, '[]')

        none_dic = Base.to_json_string(None)
        self.assertIsInstance(none_dic, list)
        self.assertEqual(none_dic, [])

        list_test = Base.from_json_string(json_dictionary)
        self.assertIsInstance(list_test, list)
        self.assertEqual(list_test[0]['width'], dictionary['width'])
        self.assertEqual(list_test[0]['height'], dictionary['height'])
        self.assertEqual(list_test[0]['x'], dictionary['x'])
        self.assertEqual(list_test[0]['y'], dictionary['y'])
        self.assertEqual(list_test[0]['id'], dictionary['id'])

    def test_base_to_and_from_json_string_square(self):
        r1 = Square(6, 6, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

        empty_dictionary = Base.to_json_string([])
        self.assertIsInstance(empty_dictionary, str)
        self.assertEqual(empty_dictionary, '[]')

        none_dic = Base.to_json_string(None)
        self.assertIsInstance(none_dic, list)
        self.assertEqual(none_dic, [])

        list_test = Base.from_json_string(json_dictionary)
        self.assertIsInstance(list_test, list)
        self.assertEqual(list_test[0]['size'], dictionary['size'])
        self.assertEqual(list_test[0]['x'], dictionary['x'])
        self.assertEqual(list_test[0]['y'], dictionary['y'])
        self.assertEqual(list_test[0]['id'], dictionary['id'])
