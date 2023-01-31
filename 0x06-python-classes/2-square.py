#!/usr/bin/python3
<<<<<<< HEAD
"""
    Module 2-square
    Define a square with Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
"""
class Square:
    """Square class with  Private instance attribute: size"""
=======
    """A square Module"""
class Square:
    """Creating class attribute with condition"""
>>>>>>> f583154531d683360b0042868b68cab24de73128
    def __init__(self, size=0):
        """Instantiation with optional size:"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
