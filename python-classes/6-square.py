#!/usr/bin/python3
"""This module creates a class Square
"""


class Square:
    """This class creates a private instance attribute size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        """This function creates a private instance size and position
        """
        self.__size = size
        self.__position = position
    
    def area(self):
        """This function returns the current square area
        """
        return self.__size ** 2
    
    def position(self):
        """This function returns the position
        """
        return self.__position
    
    @property
    def size(self):
        """This function returns the size
        """
        return self.__size

    @property
    def position(self):
        """This function returns the position
        """
        return self.__position
    
    @size.setter
    def size(self, value):
        """This function sets the size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @size.setter
    def positiong(self, value):
        """This function sets the position
        """
        if type(value) is not tuple or len(value) != 2 or type(value[0]) is not int or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
    def my_print(self):
        """This function prints the square in stdout with # characters
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
