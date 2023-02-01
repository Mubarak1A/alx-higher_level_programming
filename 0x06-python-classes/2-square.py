#!/usr/bin/python3
"""
    Module 2-square
    Define a square with Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
"""
class Square:
    """Square class with  Private instance attribute: size"""
    def __init__(self, size=0):
        """Instantiation with optional size:"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size