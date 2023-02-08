#!/usr/bin/python3
"""Module for lookup function that returns all available attribute and methods of the obj"""

def lookup(obj):
    """
        function to return all available attribute and methods of an object(the arg: obj)

        Args:
            obj (object)

        return:
            list (list of available attributes and methods)
    """
    return dir(obj)
