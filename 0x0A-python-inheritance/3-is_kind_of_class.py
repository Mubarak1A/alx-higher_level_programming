#!/usr/bin/python3
"""
    Module for function is_kind_of_class
    returns True if the object (first arg) is an instance of,
    or if the object (first arg) is an instance of a class that inherited from, the specified class (secound arg)
    otherwise False.
"""
def is_kind_of_class(obj, a_class):
    """
        function that check if the object is an instance of,
        or if the object is an instance of a class that inherited from, the specified class

        Args:
            obj (object)
            a_class (class)

        Returns:
            True (if true)
            False (if false)
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False