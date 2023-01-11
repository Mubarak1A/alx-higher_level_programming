#!/usr/bin/python3
def number_keys(a_dictionary):
    sorted_keys = sort(a_dictionary.keys())
    new_dict = {key: a_dictionary[key] for key in sorted_keys}
