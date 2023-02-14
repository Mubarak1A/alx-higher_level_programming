#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """"Square class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id, x, y, width, height)
        self.__width = size
        self.__height = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, width):
        """setter function for size"""
        self.__width = size
        self.__height = size

    def __str__(self):
        """return class description"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""
        if args is not None and len(args) > 0:
            keys = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                setatrr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.__id, "size": self.__size, "x": self.__x,
                "y": self.__y}
