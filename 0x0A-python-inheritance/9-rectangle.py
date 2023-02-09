#!/usr/bin/python3

"""Module for Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle Class inherit from BaseGeometry"""
    
    def __init__(self, width, height):
        """Class attributes"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    
    def area(self):
        """Return the area of the rectangle (width * height)"""
        return self.__width * self.__height

    def __str__(self):
        """return rectangle description"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))