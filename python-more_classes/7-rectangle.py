#!/usr/bin/python3
""" this module creates an empty class Rectangle
"""


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initializes a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ returns a string of # as a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __print__(self):
        """prints rectangle
        """
        print(str(self))

    def __repr__(self):
        """ returns a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ deletes an instance of Rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
