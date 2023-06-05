#!/usr/bin/python3
''' Unittest for class Base '''
from contextlib import AbstractContextManager
from typing import Any
import unittest
from models.rectangle import Rectangle

class TestTangles(unittest.TestCase):
    ''' Unittest for class Rectangle '''

    def test_simple_tangle(self):
        testangle = Rectangle(13, 37)
        self.assertEqual(testangle.width, 13)
        self.assertEqual(testangle.height, 37)
    
    def test_tangle_with_args(self):
        testangle = Rectangle(1, 3, 3, 7, 89)
        self.assertEqual(testangle.width, 1)
        self.assertEqual(testangle.height, 3)
        self.assertEqual(testangle.x, 3)
        self.assertEqual(testangle.y, 7)
        self.assertEqual(testangle.id, 89)

    def test_tangle_string_height(self):
        with self.assertRaises(TypeError):
            testangle = Rectangle("1", 3, 3, 7, 89)
    
    def test_tangle_string_width(self):
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, "3", 3, 7, 89)
    
    def test_tangle_string_x(self):
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, 3, "3", 7, 89)
    
    def test_tangle_string_y(self):
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, 3, 3, "7", 89)
    
    def test_tangle_negative_height(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(13, -37)
    
    def test_tangle_negative_width(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(-13, 37)
    
    def test_tangle_negative_x(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(1, 3, -3, 7, 89)
    
    def test_tangle_negative_y(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(1, 3, 3, -7, 89)
    
    def test_tangle_zero_height(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(0, 37)
    
    def test_tangle_zero_width(self):
        with self.assertRaises(ValueError):
            testangle = Rectangle(13, 0)

    def test_tangle_str_function(self):
        testangle = Rectangle(3, 7, 1, 3, 89)
        self.assertEqual(testangle.__str__(), "[Rectangle] (89) 1/3 - 3/7")
    
    def test_tangle_to_dictionary(self):
        testangle = Rectangle(1, 3, 3, 7, 89)
        self.assertEqual(testangle.to_dictionary(), {'x': 3, 'y': 7, 'id': 89, 'height': 3, 'width': 1})
    
    def test_tangle_update(self):
        testangle = Rectangle(1, 2, 3, 4, 5)
        testangle.update(1, 3, 3, 7, 89)
        self.assertEqual(testangle.width, 3)
        self.assertEqual(testangle.height, 3)
        self.assertEqual(testangle.x, 7)
        self.assertEqual(testangle.y, 89)
        self.assertEqual(testangle.id, 1)
    
    def test_tangle_update_kwargs(self):
        testangle = Rectangle(1, 2, 3, 4, 5)
        testangle.update(height=1, width=3, x=3, y=7, id=89)
        self.assertEqual(testangle.width, 3)
        self.assertEqual(testangle.height, 1)
        self.assertEqual(testangle.x, 3)
        self.assertEqual(testangle.y, 7)
        self.assertEqual(testangle.id, 89)

    def test_tangle_area(self):
        testangle = Rectangle(3, 2)
        self.assertEqual(testangle.area(), 6)
