#!/usr/bin/python3
""""Module for function write_file"""


def write_file(filename="", text=""):
    """
        function that writes to a text file (UTF8) and returns the number of
        characters written:

        Args:
            filename (txt file)
            text (sting)

        return:
            int (number of characters written)
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)

    with open("filename", encoding="utf-8") as myFile:
        my_file = myFile.read()
        
    char = 0
    for word in my_file:
        for char in word:
            char += 1
               
    return char