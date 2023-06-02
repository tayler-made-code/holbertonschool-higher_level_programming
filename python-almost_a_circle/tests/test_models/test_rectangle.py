#!/usr/bin/python3
''' Unittest for class Base '''
import unittest
from models.rectangle import Rectangle

class TestRectangleArea(unittest.TestCase):
    ''' Test cases for area '''

    def test_simple_area(self):
        testangle = Rectangle(3, 2)
        self.assertEqual(testangle.area(), 6)

    def test_area_with_args(self):
        testangle = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(testangle.area(), 56)

