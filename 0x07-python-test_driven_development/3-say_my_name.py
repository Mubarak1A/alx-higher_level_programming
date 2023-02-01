#!/usr/bin/python3
"""Module for say_my_name function

    Function: say_my_name

    return: My name is <arg1> <arg2>
"""
def say_my_name(first_name, last_name=""):
    """Compute and return a message with arg1 and arg2(My name is <arg1> <arg2>).
    
    Examples:
        >>>say_my_name("John", "Smith")
        My name is John Smith
        >>>say_my_name("Walter", "White")
        My name is Walter White
        >>>say_my_name("Bob")
        My name is Bob
        >>>try:
        ...    say_my_name(12, "White")
        ...except Exception as e:
        ...    print(e)
        first_name must be a string


    Args:
        first_name: A string representing the first arg
        last_name: A string representing the secound arg with default value "".
    returns:
        string: My name is first_name Last_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}$".format(first_name, last_name))




say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)