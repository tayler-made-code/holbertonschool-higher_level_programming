#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function
    """
    def test_max_integer(self):
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)
