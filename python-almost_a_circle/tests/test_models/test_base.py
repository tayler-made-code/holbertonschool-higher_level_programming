#!/usr/bin/python3
''' Unittest for integer_validator '''
import unittest

to_json_string = __import__('models.base').to_json_string
save_to_file = __import__('models.base').save_to_file
from_json_string = __import__('models.base').from_json_string
create = __import__('models.base').create
load_from_file = __import__('models.base').load_from_file

rec_width = __import__('models.rectangle').Rectangle.width
rec_height = __import__('models.rectangle').Rectangle.height
x = __import__('models.rectangle').Rectangle.x
y = __import__('models.rectangle').Rectangle.y
rec_id = __import__('models.rectangle').Rectangle.id
integer_validator = __import__('models.rectangle').integer_validator
area = __import__('models.rectangle').Rectangle.area
display = __import__('models.rectangle').Rectangle.display
rec_str_rep = __import__('models.rectangle').Rectangle.__str__
rec_update = __import__('models.rectangle').Rectangle.update
rec_to_dictionary = __import__('models.rectangle').Rectangle.to_dictionary

sq_size = __import__('models.square').Square.size
sq_update = __import__('models.square').Square.update
sqr_str_rep = __import__('models.square').Square.__str__
sq_to_dictionary = __import__('models.square').Square.to_dictionary

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
