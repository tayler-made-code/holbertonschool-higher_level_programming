#!/usr/bin/python3
''' this module creates a class Square that inherits from Rectangle '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' This class defines a Square inherited from Rectangle '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Construction Juntction Square's my function! '''
        self.integer_validator("size", size)
        self.__size = width = height = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        ''' returns string representation of Square '''
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )
