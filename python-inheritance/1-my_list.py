#!/usr/bin/python3
""" Module for MyList class that inherits from list """


class MyList(list):
    """ MyList class inherited from list """
    def print_sorted(self):
        """ prints a the list, but sorted in ascending order """
        print(sorted(self))
