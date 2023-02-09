#!/usr/bin/python3
""""Module for function append_write"""

import os

def append_write(filename="", text=""):
    """
        function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

        Args:
            filename (txt file)
            text (sting)

        return:
            int (number of characters added)
    """
    with open("filename", mode="a", encoding="UTF-8") as myFile:
        myFile.write(text)
    
    char = 0
    for word in text:
        for char in word:
            char += 1
    
    return char
    
    