#!/usr/bin/python3
''' Unittest for class Base '''
import unittest
from model.base import base

to_json_string = __import__('models.base').to_json_string
save_to_file = __import__('models.base').save_to_file
from_json_string = __import__('models.base').from_json_string
create = __import__('models.base').create
load_from_file = __import__('models.base').load_from_file

class TestBase(unittest.TestCase):
    ''' Test cases for base.py '''
    def to_json_string(self):
        ''' Test to_json_string '''
        self.assertEqual(to_json_string(None), "[]")
        self.assertEqual(to_json_string([]), "[]")
        self.assertEqual(to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertEqual(to_json_string([{'id': 12}, {'id': 13}]),
                         '[{"id": 12}, {"id": 13}]')
        self.assertEqual(to_json_string([{'id': 12}, {'id': 13}, {'id': 14}]),
                '[{"id": 12}, {"id": 13}, {"id": 14}]')
