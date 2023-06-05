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

class TestWidthSetter(unittest.TestCase):
    ''' Unittest for width setter '''

    def test_width_setter(self):
        testangle = Rectangle(3, 2)
        testangle.width = 10
        self.assertEqual(testangle.width, 10)
    
    def test_width_setter_with_args(self):
        testangle = Rectangle(8, 7, 0, 0, 12)
        testangle.width = 10
        self.assertEqual(testangle.width, 10)
    
    def test_width_setter_with_string(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = "Thirteen"
    
    def test_width_setter_with_negative(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(ValueError):
            testangle.width = -13
    
    def test_width_setter_with_zero(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(ValueError):
            testangle.width = 0
    
    def test_width_setter_with_float(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = 13.5
    
    def test_width_setter_with_tuple(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = (13, 37)
    
    def test_width_setter_with_dict(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = {13: 37}
    
    def test_width_setter_with_dict(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = [13, 37]
    
    def test_width_setter_with_set(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = {13, 37}
    
    def test_width_setter_with_bool(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = True
    
    def test_width_setter_with_None(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = None
    
    def test_width_setter_with_inf(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = float('inf')

    def test_width_setter_with_nan(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = float('nan')
    
    def test_width_setter_with_negative_inf(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = float('-inf')
    
    def test_width_setter_with_negative_inf(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = float('-inf')
    
    def test_width_setter_with_negative_nan(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = float('-nan')
    
    def test_width_setter_with_complex(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = complex(13, 37)
    
    def test_width_setter_with_complex(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width = complex(13, 37)
    
    def test_width_setter_with_zero_args(self):
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width()
