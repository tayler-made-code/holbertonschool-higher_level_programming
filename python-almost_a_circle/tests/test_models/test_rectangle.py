#!/usr/bin/python3
''' Unittest for class Base '''
import unittest
from models.rectangle import Rectangle
area = __import__('rectangle').Rectangle.area

class TestArea(unittest.TestCase):
    ''' Test cases for area '''

    def test_simple_area(self):
        testangle = Rectangle(3, 2)
        self.assertEqual(area(testangle), 6)

    def test_area_with_args(self):
        testangle = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(area(testangle), 56)

    def test_area_width_string(self):
        testangle = Rectangle("string", 2, 0, 0, 12)
        self.assertEqual(area(testangle), "TypeError: width must be an integer")

    def test_area_height_string(self):
        testangle = Rectangle(2, "string", 0, 0, 12)
        self.assertEqual(area(testangle), "TypeError: height must be an integer")

    def test_area_x_string(self):
        testangle = Rectangle(2, 2, "string", 0, 12)
        self.assertEqual(area(testangle), "TypeError: x must be an integer")

    def test_area_y_string(self):
        testangle = Rectangle(2, 2, 0, "string", 12)
        self.asserEqual(area(testangle), "TypeError: y must be an integer")

    def test_area_id_string(self):
        testangle = Rectangle(2, 2, 0, 0, "string")
        self.asserEqual(area(testangle), "TypeError: id must be an integer")

    def test_area_id_neg(self):
        testangle = Rectangle(2, 2, 0, 0, -1)
        self.asserEqual(area(testangle), "ValueError: id must be > 0")

    def test_area_id_zero(self):
        testangle = Rectangle(2, 2, 0, 0, 0)
        self.assertEqual(area(testangle), "ValueError: id must be > 0")

    def test_area_y_neg(self):
        testangle = Rectangle(2, 2, 0, -1, 12)
        self.assertEqual(area(testangle), "ValueError: y must be >= 0")

    def test_area_x_neg(self):
        testangle = Rectangle(2, 2, -1, 0, 12)
        self.assertEqual(area(testangle), "ValueError: x must be >= 0")

    def test_area_height_neg(self):
        testangle = Rectangle(2, -1, 0, 0, 12)
        self.assertEqual(area(testangle), "ValueError: height must be > 0")

    def test_area_width_neg(self):
        testangle = Rectangle(-1, 2, 0, 0, 12)
        self.assertEqual(area(testangle), "ValueError: width must be > 0")

    def test_area_height_zero(self):
        testangle = Rectangle(2, 0, 0, 0, 12)
        self.assertEqual(area(testangle), "ValueError: height must be > 0")

    def test_area_width_zero(self):
        testangle = Rectangle(0, 2, 0, 0, 12)
        self.assertEqual(area(testangle), "ValueError: width must be > 0")

    def test_area_width_float(self):
        testangle = Rectangle(2.5, 2, 0, 0, 12)
        self.assertEqual(area(testangle), "TypeError: width must be an integer")

