#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
idx2 = -1
idx3 = 9
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
print("Element at index {:d} is {}".format(idx2, element_at(my_list, idx2)))
print("Element at index {:d} is {}".format(idx3, element_at(my_list, idx3)))
