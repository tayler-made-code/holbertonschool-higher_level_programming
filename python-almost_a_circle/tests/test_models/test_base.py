#!/usr/bin/python3
''' Unittest for integer_validator '''
import unittest
from models.basdde import Base


class TestSaveToFile(unittest.TestCase):
    ''' Unittest for save_to_file method '''

    def test_save_to_file(self):
        Base._Base__nb_objects = 0
        r1 = Base(10, 7)
        r2 = Base(2)
        list_rectangles_input = [r1, r2]
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input[0].id,
                         list_rectangles_output[0].id)
        self.assertEqual(list_rectangles_input[1].id,
                         list_rectangles_output[1].id)
    
    def test_save_to_file_empty(self):
        Base._Base__nb_objects = 0
        list_rectangles_input = []
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input, list_rectangles_output)
    
    def test_save_to_file_None(self):
        Base._Base__nb_objects = 0
        list_rectangles_input = None
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input, list_rectangles_output)
    
    def test_save_to_file_more(self):
        ''' Test save_to_file method with more than 1 object '''
        Base._Base__nb_objects = 0
        r1 = Base(10, 7)
        r2 = Base(2)
        r3 = Base(5)
        list_rectangles_input = [r1, r2, r3]
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input[0].id,
                            list_rectangles_output[0].id)
        self.assertEqual(list_rectangles_input[1].id,
                            list_rectangles_output[1].id)
        self.assertEqual(list_rectangles_input[2].id,
                            list_rectangles_output[2].id)

class TestBaseToJsonString(unittest.TestCase):
    ''' Unittest for to_json_string method '''

    def test_to_json_string(self):
        ''' Test to_json_string method '''
        json_string = '[{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}]'
        list_input = Base.to_json_string(json_string)
        list_output = '[{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}]'
        self.assertEqual(list_input, list_output)
    
    def test_to_json_string_empty(self):
        ''' Test to_json_string method with empty string '''
        json_string = ''
        list_input = Base.to_json_string(json_string)
        list_output = '[]'
        self.assertEqual(list_input, list_output)
    
    def test_to_json_string_None(self):
        ''' Test to_json_string method with None '''
        json_string = None
        list_input = Base.to_json_string(json_string)
        list_output = '[]'
        self.assertEqual(list_input, list_output)
    
    def test_to_json_string_more(self):
        ''' Test to_json_string method with more than 1 object '''
        json_string = '[{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}, {"id": 8, "width": 2, "height": 8}]'
        list_input = Base.to_json_string(json_string)
        list_output = '[{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}, {"id": 8, "width": 2, "height": 8}]'
        self.assertEqual(list_input, list_output)

class TestBase__init__(unittest.TestCase):
    ''' Unittest for __init__ method '''

    def test__init__id(self):
        ''' Test __init__ method with id '''
        Base._Base__nb_objects = 0
        r1 = Base(10)
        self.assertEqual(r1.id, 10)

    def test__init__id_None(self):
        ''' Test __init__ method with id None '''
        Base._Base__nb_objects = 0
        r1 = Base(None)
        self.assertEqual(r1.id, 1)
    
    def test__init__id_more(self):
        ''' Test __init__ method with more than 1 object '''
        Base._Base__nb_objects = 0
        r1 = Base(10)
        r2 = Base(7)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r2.id, 7)
    
    def test__init__id_None_more(self):
        ''' Test __init__ method with id None and more than 1 object '''
        Base._Base__nb_objects = 0
        r1 = Base(None)
        r2 = Base(None)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

class TestBaseFromJsonString(unittest.TestCase):
    ''' Unittest for from_json_string method '''

    def test_from_json_string(self):
        ''' Test from_json_string method '''
        json_string = '[{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}]'
        list_input = Base.from_json_string(json_string)
        list_output = [{'id': 89, 'width': 10, 'height': 4},
                          {'id': 7, 'width': 1, 'height': 7}]
        self.assertEqual(list_input, list_output)
    
    def test_from_json_string_empty(self):
        ''' Test from_json_string method with empty string '''
        json_string = ''
        list_input = Base.from_json_string(json_string)
        list_output = []
        self.assertEqual(list_input, list_output)
    
    def test_from_json_string_None(self):
        ''' Test from_json_string method with None '''
        json_string = None
        list_input = Base.from_json_string(json_string)
        list_output = []
        self.assertEqual(list_input, list_output)
    
    def test_from_json_string_more(self):
        ''' Test from_json_string method with more than 1 object '''
        json_string = '[{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}, {"id": 8, "width": 2, "height": 8}]'
        list_input = Base.from_json_string(json_string)
        list_output = [{'id': 89, 'width': 10, 'height': 4},
                            {'id': 7, 'width': 1, 'height': 7},
                            {'id': 8, 'width': 2, 'height': 8}]
        self.assertEqual(list_input, list_output)

class TestBaseCreate(unittest.TestCase):
    ''' Unit test for create method '''

    def test_create_rectangle(self):
        ''' Test create method with Rectangle '''
        Base._Base__nb_objects = 0
        r1 = Base(10, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Base.create(**r1_dictionary)
        self.assertEqual(r1.id, r2.id)
    
    def test_create_square(self):
        ''' Test create method with Square '''
        Base._Base__nb_objects = 0
        s1 = Base(10)
        s1_dictionary = s1.to_dictionary()
        s2 = Base.create(**s1_dictionary)
        self.assertEqual(s1.id, s2.id)

    def test_create_more(self):
        ''' Test create method with more than 1 object '''
        Base._Base__nb_objects = 0
        r1 = Base(10, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Base.create(**r1_dictionary)
        self.assertEqual(r1.id, r2.id)
        s1 = Base(10)
        s1_dictionary = s1.to_dictionary()
        s2 = Base.create(**s1_dictionary)
        self.assertEqual(s1.id, s2.id)
    
    def test_create_None(self):
        ''' Test create method with None '''
        Base._Base__nb_objects = 0
        r1 = Base(None)
        r1_dictionary = r1.to_dictionary()
        r2 = Base.create(**r1_dictionary)
        self.assertEqual(r1.id, r2.id)

class TestBaseLoadFromFile(unittest.TestCase):
    ''' Unittest for load_from_file method '''

    def test_load_from_file(self):
        ''' Test load_from_file method '''
        Base._Base__nb_objects = 0
        r1 = Base(10)
        r2 = Base(7)
        list_rectangles_input = [r1, r2]
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input[0].id,
                         list_rectangles_output[0].id)
        self.assertEqual(list_rectangles_input[1].id,
                         list_rectangles_output[1].id)
    
    def test_load_from_file_empty(self):
        ''' Test load_from_file method with empty list '''
        Base._Base__nb_objects = 0
        list_rectangles_input = []
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input, list_rectangles_output)
    
    def test_load_from_file_None(self):
        ''' Test load_from_file method with None '''
        Base._Base__nb_objects = 0
        list_rectangles_input = None
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input, list_rectangles_output)
    
    def test_load_from_file_more(self):
        ''' Test load_from_file method with more than 1 object '''
        Base._Base__nb_objects = 0
        r1 = Base(10)
        r2 = Base(7)
        r3 = Base(5)
        list_rectangles_input = [r1, r2, r3]
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input[0].id,
                         list_rectangles_output[0].id)
        self.assertEqual(list_rectangles_input[1].id,
                         list_rectangles_output[1].id)
        self.assertEqual(list_rectangles_input[2].id,
                         list_rectangles_output[2].id)
