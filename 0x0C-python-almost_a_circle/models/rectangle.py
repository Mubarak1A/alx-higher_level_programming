#!/usr/bin/python3
"""Module for Rectangle class"""
from base import Base


class Rectangle(Base):
    """"Rectangles class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """getter for __width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter function for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter for __height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter function for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter for __x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter function for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for __y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter function for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__heigth

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print('', end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """return class description"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.__id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""
        if args is not None and len(args) > 0:
            keys = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                setatrr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.__id, "width": self.__width,
                "heigth": self.__height, "x": self.__x, "y": self.__y}
