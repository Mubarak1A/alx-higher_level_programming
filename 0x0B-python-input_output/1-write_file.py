#!/usr/bin/python3
""""Module for function write_file"""

import os

def write_file(filename="", text=""):
    """
        function that writes to a text file (UTF8) and returns the number of characters written:

        Args:
            filename (txt file)
            text (sting)

        return:
            int (number of characters written)
    """
    with open("filename", mode="w", encoding="UTF-8") as myFile:
        myFile.write(text)
    
    char = 0
    for word in text:
        for char in word:
            char += 1
    
    return char

    