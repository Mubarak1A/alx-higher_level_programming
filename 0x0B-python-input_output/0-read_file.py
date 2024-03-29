#!/usr/bin/python3
""""Module for function read_file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:

        Args:
            filename (txt file)
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
