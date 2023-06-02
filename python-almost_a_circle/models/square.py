#!/usr/bin/python3
''' this module creates a class Square that inherits from Rectangle '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' This class defines a Square inherited from Rectangle '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
        self.size = 

    def __str__(self):
        ''' returns string representation of Square '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
        self.size)
