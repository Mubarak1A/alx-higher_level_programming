#!/usr/bin/python3
""""Module for function from_json_string"""

import json

def from_json_string(my_str):
    """
        function that returns an object (Python data structure) represented by a JSON string:
        Args:
            my_str (JSON string)

        return:
            an object (Python data structure)
    """
    return json.load(my_str)
    