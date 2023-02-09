#!/usr/bin/python3
""""Module for function to_json_string"""

import json

def to_json_string(my_obj):
    """
         function that returns the JSON representation of an object (string):

        Args:
            my_obj (object)

        return:
            JSON format (kind of dictinary look alike)
    """
    return vars(my_obj)
    
    