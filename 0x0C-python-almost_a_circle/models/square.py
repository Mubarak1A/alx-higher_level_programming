#!/usr/bin/python3
"""Module for Square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """"Square class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id, x, y, width, height)
        self.width = size
        self.height = size

    @property
    def size(self):
        """getter for size"""
        return self.size

    @size.setter
    def size(self, width):
        """setter function for size"""
        self.width = size
        self.height = size

    def __str__(self):
        """return class description"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                       self.y, self.width)
