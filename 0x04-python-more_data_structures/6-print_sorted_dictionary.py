#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = set(sorted(a_dictionary.keys()))
    new_dict = {key: a_dictionary[key] for key in sorted_keys}

    return new_dict
