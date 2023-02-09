#!/usr/bin/python3

"""Module for Square that inherits from Rectangle (9-rectangle.py):"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Square Class inherit from BaseGeometry"""
    
    def __init__(self, size):
        """Class attributes"""
        self.__size = size
        self.integer_validator("size", size)
    
    def area(self):
        """Return the area of the Square (size ** 2)"""
        return self.__size ** 2