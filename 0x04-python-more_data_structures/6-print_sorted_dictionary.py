#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = [key for key in (a_dictionary.keys())]
    sorted_keys.sort()
    new_dict = {key: a_dictionary[key] for key in sorted_keys}

    for key in new_dict.keys()
        print("{}: {}".format(key, new_dict[key])
