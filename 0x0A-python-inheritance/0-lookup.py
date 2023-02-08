#!/usr/bin/python3
"""
    Module for lookup function

    args: obj (an object)
    returns: all attribute and methods of the obj
"""
def lookup(obj):
    """
        function to return all available attribute and methods of an object(the arg: obj)
    """
    return dir(obj)
    