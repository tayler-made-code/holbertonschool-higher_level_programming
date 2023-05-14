#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    seeing_double = {}
    for key, value in a_dictionary.items():
        seeing_double[key] = value * 2
    return seeing_double
