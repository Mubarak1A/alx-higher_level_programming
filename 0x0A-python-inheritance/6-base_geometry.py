#!/usr/bin/python3
"""
    Module for a class BaseGeometry
    with a Public instance method: def area(self):
"""

class BaseGeometry():
    """Class with no attributes"""

    def area(self):
        """
             raises an Exception with the message area() is not implemented (as their is no attribute)
        """
        raise Exception("area() is not implemented")