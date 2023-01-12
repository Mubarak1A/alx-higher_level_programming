#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        for i in a_dictionary.keys():
            if a_dictionary[i] == max(a_dictionary.values()):
                return i
