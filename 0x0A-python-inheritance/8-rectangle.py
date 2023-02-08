#!/usr/bin/python3

"""
    Module of a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle Class inherit from BaseGeometry"""
    
    def __init__(self, width, height):
        """Class attributes"""
        self.width = width
        self.height = height
        