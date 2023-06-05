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

    def test_area_with_string(self):
        squample = Square(4)
        with self.assertRaises(TypeError):
            squample.area("1")

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
            squample.size = "1"

    def test_size_setter_with_negative(self):
        squample = Square(4)
        with self.assertRaises(ValueError):
            squample.size = -13

    def test_size_setter_with_zero(self):
        squample = Square(4)
        with self.assertRaises(ValueError):
            squample.size = 0

class TestXSetter(unittest.TestCase):
    ''' Test cases for x setter '''

    def test_x_setter(self):
        squample = Square(3, 5)
        self.assertEqual(squample.x, 5)

    def test_x_setter_with_args(self):
        squample = Square(1, 3, 3, 7)
        self.assertEqual(squample.x, 3)

    def test_x_setter_with_string(self):
        squample = Square(4)
        with self.assertRaises(TypeError):
            squample.x = "Thirteen"

    def test_x_setter_with_negative(self):
        squample = Square(4)
        with self.assertRaises(ValueError):
            squample.x = -13

    def test_x_setter_with_zero(self):
        squample = Square(4)
        squample.x = 0
        self.assertEqual(squample.x, 0)
        squample = Square(4)
        with self.assertRaises(TypeError):
            squample.x()

class TestYSetter(unittest.TestCase):
    ''' Test cases for y setter '''

    def test_y_setter(self):
        squample = Square(3, 5, 7)
        self.assertEqual(squample.y, 7)

    def test_y_setter_with_args(self):
        squample = Square(1, 3, 3, 7)
        self.assertEqual(squample.y, 3)

    def test_y_setter_with_string(self):
        squample = Square(1, 3, 3, 7)
        with self.assertRaises(TypeError):
            squample.y = "Thirteen"

    def test_y_setter_with_negative(self):
        squample = Square(1, 3, 3, 7)
        with self.assertRaises(ValueError):
            squample.y = -13

    def test_y_setter_with_zero(self):
        squample = Square(1, 3, 3, 7)
        squample.y = 0
        self.assertEqual(squample.y, 0)

        squample = Square(4)
        with self.assertRaises(TypeError):
            squample.y()

class TestSTR(unittest.TestCase):
    ''' Test cases for __str__ '''
    def test_str(self):
        squample = Square(1, 3, 3, 7)
        self.assertEqual(squample.__str__(), "[Square] (7) 3/3 - 1")

    def test_str_with_string(self):
        squample = Square(1, 3, 3, 7)
        with self.assertRaises(TypeError):
            squample.__str__("1")

class TestSquareUpdate(unittest.TestCase):
    ''' Test cases for update '''
  
    def test_update(self):
        squample = Square(1, 3, 3, 7)
        squample.update(9, 8, 7, 6)
        self.assertEqual(squample.__str__(), "[Square] (9) 7/6 - 8")
    
    def test_update_with_kwargs(self):
        squample = Square(1, 3, 3, 7)
        squample.update(id=9, size=8, x=7, y=6)
        self.assertEqual(squample.__str__(), "[Square] (9) 7/6 - 8")
    
    def test_update_with_args_and_kwargs(self):
        squample = Square(1, 3, 3, 7)
        squample.update(9, 8, 7, 6, id=10, size=9, x=8, y=7)
        self.assertEqual(squample.__str__(), "[Square] (9) 7/6 - 8")
    
    def test_update_with_no_args(self):
        squample = Square(1, 3, 3, 7)
        squample.update()
        self.assertEqual(squample.__str__(), "[Square] (7) 3/3 - 1")
    
    def test_update_with_string(self):
        squample = Square(1, 3, 3, 7)
        with self.assertRaises(TypeError):
            squample.update("Nine", "Eight", "Seven", "Six")
    
    def test_update_with_negative(self):
        squample = Square(1, 3, 3, 7)
        with self.assertRaises(ValueError):
            squample.update(-9, -8, -7, -6)
    
    def test_update_with_zero(self):
        squample = Square(1, 3, 3, 7)
        with self.assertRaises(ValueError):
            squample.update(0, 0, 0, 0)

    def test_update_with_strings(self):
        squample = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            squample.update("One", "Three", "Three", "Seven")
