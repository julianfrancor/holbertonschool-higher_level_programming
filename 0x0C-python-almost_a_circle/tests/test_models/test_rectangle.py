#!/usr/bin/python3

import unittest
import pep8
import sys
from io import StringIO
import os
import json
from models.rectangle import Rectangle, Base

""" import:
    all the modules needed (unittest and pep8)
    all the classes and methods to be tested
"""

"""
    Test suite for Almost a circle project to test:
        the methods of the Rectangle class

    Here we have a collection of test cases, test suites or both
    All this tests should be executed together
    we create a test case based on the Class "unittest.TestCase"
"""


class TestRectangle(unittest.TestCase):
    """
    class to test Rectangle Class with Unit test
    """

    def setUp(self):
        """The setUp() and tearDown() methods allow you
        to define instructions that will be executed
        before and after each test method"""
        Base._Base__nb_objects = 0

    def test_rectangle_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_id(self):
        """Test when id is/isn't passed"""
        r1 = Rectangle(5, 3)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        r3 = Rectangle(4, 9)
        self.assertEqual(r3.id, 2)

    def test_raise_exceptions(self):
        """Test raises correct errors
        when passed incorrect imputs"""

        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(TypeError):
            Rectangle("8", 4)
        with self.assertRaises(ValueError):
            Rectangle(-8, 4)
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Rectangle(-10, 2)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, 3, -1)
        self.assertTrue("y must be >= 0" in str(cm.exception))

    def test_area(self):
        """Test area to display correct values"""
        r4 = Rectangle(3, 2)
        r5 = Rectangle(2, 10)
        r6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r4.area(), 6)
        self.assertEqual(r5.area(), 20)
        self.assertEqual(r6.area(), 56)

    def test_display(self):
        """Test the correct display of a rectanlge with # """
        r7 = Rectangle(4, 6)
        old_stdout = sys.stdout
        temp_out = StringIO()
        sys.stdout = temp_out
        r7.display()
        self.assertEqual(sys.stdout.getvalue(),
                         "####\n####\n####\n####\n####\n####\n")
        r8 = Rectangle(2, 3, 2, 2)
        old_stdout = sys.stdout
        temp_out = StringIO()
        sys.stdout = temp_out
        r8.display()
        self.assertEqual(sys.stdout.getvalue(),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_update_1(self):
        """Tests """
        r9 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r9.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r9.update(89)
        self.assertEqual(r9.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r9.update(89, 2)
        self.assertEqual(r9.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r9.update(89, 2, 3)
        self.assertEqual(r9.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r9.update(89, 2, 3, 4)
        self.assertEqual(r9.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r9.update(89, 2, 3, 4, 5)
        self.assertEqual(r9.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r10 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r10.__str__(), "[Rectangle] (2) 10/10 - 10/10")
        r10.update(id=8, width=9, height=3, x=20, y=30)
        self.assertEqual(r10.__str__(), "[Rectangle] (8) 20/30 - 9/3")

    def test_to_dictionary(self):
        """Test to check if method to_dictionary returns a valid
        dictionary representation of Rectangle"""
        r11 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r11.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        r11_dictionary = r11.to_dictionary()
        self.assertEqual(r11_dictionary, {'x': 1, 'y': 9, 'id': 1,
                                          'height': 2, 'width': 10})
        self.assertIs(type(r11_dictionary), dict)

    def test_save_to_file(self):
        """Test to check if writes the JSON string representation of
        list_objs to a file"""
        r12 = Rectangle(10, 7, 2, 8)
        r13 = Rectangle(2, 4)
        Rectangle.save_to_file([r12, r13])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"y": 8, "x": 2,
                                                        "id": 1, "width": 10,
                                                        "height": 7},
                                                       {"y": 0,
                                                        "x": 0, "id": 2,
                                                        "width": 2,
                                                        "height": 4}])
        os.remove("Rectangle.json")
