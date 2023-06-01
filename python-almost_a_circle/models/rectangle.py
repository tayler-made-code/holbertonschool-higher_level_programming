#!/usr/bin/python3
''' this module creates a class Rectangle that inherits from base '''
from models.base import Base


class Rectangle(Base):
    ''' This class defines a Rectangle inherited from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        ''' gets width of rectangle '''
        return self.__width

    @property
    def height(self):
        ''' gets height of rectangle '''
        return self.__height

    @property
    def x(self):
        ''' gets x of rectangle '''
        return self.__x

    @property
    def y(self):
        ''' gets y of rectangle '''
        return self.__y

    @width.setter
    def width(self, value):
        ''' sets width of rectangle '''
        self.__width = value

    @height.setter
    def height(self, value):
        ''' sets height of rectangle '''
        self.__height = value

    @x.setter
    def x(self, value):
        ''' sets x of rectangle '''
        self.__x = value

    @y.setter
    def y(self, value):
        ''' sets y of rectangle '''
        self.__y = value
