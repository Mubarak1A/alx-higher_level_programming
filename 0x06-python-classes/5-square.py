#!/usr/bin/python3
    """A square Module"""
class Square:
    """Class attribute with getter and setter"""
    def __init__(self, size=0):
        self.__size = size

    # Property
    @property
    def size(self):
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    """class Method that return square area"""
    def area(self):
        return self.__size ** 2

   """Class Method that print # on new line for size times"""
    def my_print(self):
        size = self.__size

        if size == 0:
            print()

        for row in range(size):
            print('#' * size)
