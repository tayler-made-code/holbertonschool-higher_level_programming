#!/usr/bin/python3
''' Unittest for class Square '''
import unittest
from models.square import Square


class TestSquareArea(unittest.TestCase):
    ''' Test cases for area '''

    def test_simple_area(self):
        squample = Square(3)
        self.assertEqual(squample.area(), 9)

    def test_area_with_args(self):
        squample = Square(8, 0, 0, 12)
        self.assertEqual(squample.area(), 64)

class TestSizeSetter(unittest.TestCase):
    ''' Test cases for size setter '''

    def test_size_setter(self):
        squample = Square(3)
        squample.size = 5
        self.assertEqual(squample.size, 5)

    def test_size_setter_with_args(self):
        squample = Square(8, 0, 0, 12)
        squample.size = 10
        self.assertEqual(squample.size, 10)

    def test_size_setter_with_string(self):
        squample = Square(4)
        with self.assertRaises(TypeError):
            squample.size = "Thirteen"

    def test_size_setter_with_negative(self):
        squample = square(4)
        with self.assertRaises(ValueError):
            squample.size = "-13"
