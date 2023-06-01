#!/usr/bin/python3
''' Base class for all other classes '''


class Base:
    ''' Base class for all other classes '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Construction Junction, What's your function! '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
