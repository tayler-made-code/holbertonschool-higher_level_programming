#!/usr/bin/python3
''' Unittest for class Base '''
from contextlib import AbstractContextManager
from typing import Any
import unittest
from models.rectangle import Rectangle

class TestTangles(unittest.TestCase):
    ''' Unittest for class Rectangle '''

    def test_simple_tangle(self):
        ''' Test simple rectangle '''
        testangle = Rectangle(13, 37)
        self.assertEqual(testangle.width, 13)
        self.assertEqual(testangle.height, 37)
    
    def test_tangle_with_args(self):
        ''' Test rectangle with args '''
        testangle = Rectangle(1, 3, 3, 7, 89)
        self.assertEqual(testangle.width, 1)
        self.assertEqual(testangle.height, 3)
        self.assertEqual(testangle.x, 3)
        self.assertEqual(testangle.y, 7)
        self.assertEqual(testangle.id, 89)

    def test_tangle_string_height(self):
        ''' Test rectangle with string '''
        with self.assertRaises(TypeError):
            testangle = Rectangle("1", 3, 3, 7, 89)
    
    def test_tangle_string_width(self):
        ''' Test rectangle with string '''
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, "3", 3, 7, 89)
    
    def test_tangle_string_x(self):
        ''' Test rectangle with string '''
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, 3, "3", 7, 89)
    
    def test_tangle_string_y(self):
        ''' Test rectangle with string '''
        with self.assertRaises(TypeError):
            testangle = Rectangle(1, 3, 3, "7", 89)
    
    def test_tangle_negative_height(self):
        ''' Test rectangle with negative '''
        with self.assertRaises(ValueError):
            testangle = Rectangle(-13, 37)
    
    def test_tangle_negative_width(self):
        ''' Test rectangle with negative '''
        with self.assertRaises(ValueError):
            testangle = Rectangle(-13, 37)
    
    def test_tangle_negative_x(self):
        ''' Test rectangle with negative '''
        with self.assertRaises(ValueError):
            testangle = Rectangle(1, 3, -3, 7, 89)
    
    def test_tangle_negative_y(self):
        ''' Test rectangle with negative '''
        with self.assertRaises(ValueError):
            testangle = Rectangle(1, 3, 3, -7, 89)
    
    def test_tangle_zero_height(self):
        ''' Test rectangle with zero '''
        with self.assertRaises(ValueError):
            testangle = Rectangle(0, 37)
    
    def test_tangle_zero_width(self):
        ''' Test rectangle with zero '''
        with self.assertRaises(ValueError):
            testangle = Rectangle(13, 0)

