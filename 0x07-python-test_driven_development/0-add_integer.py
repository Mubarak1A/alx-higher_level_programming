#!/usr/bin/python3
"""Module for addition function

    Function: add_integer

    return: addition of two integer argument
"""
def add_integer(a, b=98):
    """Compute and return the sum of two integer/float arguments.
    
    Examples:
        >>>add_integer(4.0, 2)
        6
        >>>add_integer(4, -2)
        2
        >>>add_integer(4.0, -2.0)
        2
        >>>add_integer(2)
        100

    Args:
        a (int/float): A number representing the first arg
        b (int/float): A number representing the secound arg with default value 98.
    returns:
        int: Sum of the two args 
    """
    if(type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if(type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b

