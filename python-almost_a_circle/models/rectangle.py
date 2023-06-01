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
        return self.width

    @property
    def height(self):
        ''' gets height of rectangle '''
        return self.height

    @property
    def x(self):
        ''' gets x of rectangle '''
        return self.x

    @property
    def y(self):
        ''' gets y of rectangle '''
        return self.y

    @width.setter
    def width(self, value):
        ''' sets width of rectangle '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
            self.__width = value

    @height.setter
    def height(self, value):
        ''' sets height of rectangle '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
            self.__height = value

    @x.setter
    def x(self, value):
        ''' sets x of rectangle '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
            self.__x = value

    @y.setter
    def y(self, value):
        ''' sets y of rectangle '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
            self.__y = value
