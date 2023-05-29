#!/usr/bin/python3
""" Module for MyList class """


class MyList(list):
    """ MyList class """
    def print_sorted(self):
        """ prints a the list, but sorted in ascending order """
        print(sorted(self))
