#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntiger(unittest.TestCase):
	def test_none_value(self):
		'''
			Testing when None is passed
		'''
		with self.assertRaises(TypeError):
			max_integer(None)

	def test_right_output(self):
		'''
			Testing the right output
		'''
		self.assertEqual(max_integer([3, 5, 6, 12]), 12)

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
		self.assertEqual(max_integer([]), 12)

	def test_max_zero(self):
		result = max_integer([0])
		self.assertEqual(result, 0)

	def test_max_only(self):
		result = max_integer([4])
		self.assertEqual(result, 4)

	def test_max_onenegative(self):
		result = max_integer([-4])
		self.assertEqual(result, -4)

	def test_max_twoint(self):
		result = max_integer([3, 6])
		self.assertEqual(result, 6)

	def test_max_negatives(self):
		result = max_integer([-6, -7, -15])
		self.assertEqual(result, -6)

	def test_max_onezero(self):
		result = max_integer([8, 0, 3])
		self.assertEqual(result, 8)

	def test_max_float(self):
		result = max_integer([8, 10.5, 3])
		self.assertEqual(result, 10.5)

	def test_max_negfloat(self):
		result = max_integer([8, -10.5, 3])
		self.assertEqual(result, 8)

	def test_max_zeros(self):
		result = max_integer([0, 0, 0])
		self.assertEqual(result, 0)

	def test_max_string(self):
		result = max_integer(["cucu"])
		self.assertEqual(result, "cucu")

	def test_max_morestrings(self):
		result = max_integer(["cucu", "hp", "x"])
		self.assertEqual(result, "x")

	def test_max_error(self):
		result = ["cucu", 5.5, 6]
		with self.assertRaises(TypeError):
			max_integer(result)