#!/usr/bin/python3
from sys import argv
''' access command line arguments '''
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
''' creates an Object from a “JSON file” '''
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
''' writes an Object to a text file, using a JSON representation '''

filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except:
    my_list = []

for i in range(1, len(argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
