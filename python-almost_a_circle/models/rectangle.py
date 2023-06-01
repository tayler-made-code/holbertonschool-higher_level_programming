#!/usr/bin/python3
''' this module creates a class Rectangle that inherits from base '''
Base = __import__('base').Base


class Rectangle(Base):
    ''' This class defines a Rectangle '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
