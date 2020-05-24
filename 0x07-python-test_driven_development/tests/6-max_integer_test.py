#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntiger(unittest.TestCase):
	"""
	class to test  max_intiger function
	with Unit test
	"""

	def test_right_output(self):
		'''
			Testing the right output
		'''
		self.assertEqual(max_integer([3, 5, 6, 12]), 12)

	def test_negatives(self):
		'''
			Testing negative intigers
		'''
		self.assertEqual(max_integer([3, -5, -6, 12]), 12)

	def test_no_parameter(self):
		'''
			Testing no parameter given
		'''
		self.assertIsNone(max_integer())

	def test_equal_valuas(self):
		'''
			Testing same values
		'''
		self.assertEqual(max_integer([4, 4, 4, 4]), 4)

	def test_not_intigers(self):
		'''
			Testing no intigers given
		'''
		with self.assertRaises(TypeError):
			max_integer(["hola", "mundo", 4, 7])

	def test_parameter_zero(self):
		'''
			Testing when zero is passed
		'''
		self.assertEqual(max_integer([0]), 0)

	def test_no_parameter(self):
		'''
			Testing when no parameter is passed
		'''
		self.assertEqual(max_integer([]), None)

	def test_only_strings(self):
		'''
			Testing only strings passed
		'''
		self.assertEqual(max_integer(["hello", "string2", "string3", "x"]), "x")
