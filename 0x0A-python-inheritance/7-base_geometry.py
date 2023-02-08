#!/usr/bin/python3
"""
    Module for a class BaseGeometry
    with Public instance method:
        def area(self):
        def integer_validator(self, name, value):
"""

class BaseGeometry():
    """Class with no attributes"""

    def area(self):
        """
             raises an Exception with the message area() is not implemented (as their is no attribute)
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))