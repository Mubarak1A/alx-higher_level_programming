#!/usr/bin/python3
"""Module for Rectanglr class"""
from base import Base


class Rectangle(Base):
    """"Rectangles class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for __width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter function for width"""
        self.__width = width

    @property
    def height(self):
        """getter for __height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter function for height"""
        self.__height = height

    @property
    def x(self):
        """getter for __x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter function for x"""
        self.__x = x

    @property
    def y(self):
        """getter for __y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter function for y"""
        self.__y = y
