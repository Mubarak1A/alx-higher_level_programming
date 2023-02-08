#!/usr/bin/python3
"""
    Module for function inherits_from
    returns True if the object (first arg) is an instance of a class (secound arg)
    that inherited (directly or indirectly) from the specified class
    otherwise False.
"""
def inherits_from(obj, a_class):
    """
        function that check if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class

        Args:
            obj (object)
            a_class (class)

        returns:
            True (if true)
            False (if false)
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
