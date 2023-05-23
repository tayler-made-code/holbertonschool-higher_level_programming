#!/usr/bin/python3
""" this module creates an empty class Rectangle
"""


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ initializes a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets width of rectangle
        """
        return self.__width
    
    @property
    def height(self):
        """ gets height of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ sets width of rectangle
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height of rectangle
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
