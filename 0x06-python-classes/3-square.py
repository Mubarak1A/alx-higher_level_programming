#!/usr/bin/python3
    """A square Module"""
class Square:
    """Creating class attribute with condition"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    """Class Method"""
    def area(self):
        size = self.__size
        return size * size
