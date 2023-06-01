#!/usr/bin/python3
''' this module creates a class Rectangle that inherits from base '''
from models.base import Base


class Rectangle(Base):
    ''' This class defines a Rectangle inherited from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        ''' gets width of rectangle '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' sets width of rectangle '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' gets height of rectangle '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' sets height of rectangle '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' gets x of rectangle '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' sets x of rectangle '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' gets y of rectangle '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' sets y of rectangle '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def integer_validator(self, name, value):
        ''' validates a value during instantiation '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        ''' returns the area of a rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' prints the rectangle to stdout '''
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        ''' returns a string representation of a rectangle '''
        return "[Rectangle]" ({}) {}/{} - {}/{}".format(
            self.id, self.__y, self.__x, self.__width, self.__height
        )
