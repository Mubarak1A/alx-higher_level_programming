#!/usr/bin/python3
"""
    Module for is_same_class function
    that returns True if the object (first arg) is exactly an instance of the specified class (second arg)
    otherwise False
"""
def is_same_class(obj, a_class):
    """
         function to check if an object is exactly an instance of a specified class

        Args:
            obj (object), a_class (class)

        returns:
            True (if true)
            False (if false)
    """
    return isinstance(obj, a_class)
