#!/usr/bin/python3
''' this module creates a class Square that inherits from Rectangle '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' This class defines a Square inherited from Rectangle '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Construction Juntction Square's my function! '''
        self.integer_validator("width", size)
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' returns string representation of Square '''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
            )

    @property
    def size(self):
        ''' size getter '''
        return self.width

    @size.setter
    def size(self, value):
        ''' size setter '''
        self.integer_validator("width", value)
        self.width = value
        self.height = value
