#!/usr/bin/python3

"""
    Module for MyList class,
    that inherit from base class list
    with a Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
"""

class MyList(list):
    """child class, inherited from class list"""
    def print_sorted(self):
        """
            Public instance method
            prints the list in sorted (ascending sort)
        """
        print(sorted(self))