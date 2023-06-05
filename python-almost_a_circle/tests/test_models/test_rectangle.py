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
    
        testangle = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            testangle.width()

class TestRectangleUpdate(unittest.TestCase):
    ''' Unittest for update '''

    def test_update(self):
        testangle = Rectangle(1, 3, 3, 7)
        testangle.update(89, 3, 7, 1, 3)
        self.assertEqual(testangle.__str__(), "[Rectangle] (89) 1/3 - 3/7")

    def test_update_with_kwargs(self):
        testangle = Rectangle(10, 10, 10, 10, 10)
        testangle.update(id=89, width=3, height=7, x=1, y=3)
        self.assertEqual(testangle.__str__(), "[Rectangle] (89) 1/3 - 3/7")

    def test_update_with_args_and_kwargs(self):
        testangle = Rectangle(1, 3, 3, 7)
        testangle.update(89, 1, 2, 3, 4, id=90, width=2, height=3, x=4, y=5)
        self.assertEqual(testangle.__str__(), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_with_no_string(self):
        testangle = Rectangle(1, 3, 3, 7)
        with self.assertRaises(TypeError):
            testangle.update("Eighty-Nine", "Three", "Seven", "One", "Three")

    def test_update_with_negative(self):
        testangle = Rectangle(1, 3, 3, 7)
        with self.assertRaises(ValueError):
            testangle.update(-89, -3, -7, -1, -3)

    def test_update_with_zero(self):
        testangle = Rectangle(1, 3, 3, 7)
        with self.assertRaises(ValueError):
            testangle.update(0, 0, 0, 0, 0)
