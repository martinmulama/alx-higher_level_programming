#!/usr/bin/python3
# 1-write_file.py
# Martin <martin.mulama@yahoo.com>
""" Module that writes a string to a tct file and returns no of characters written """

def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename: The name of file to open.
        text: The text write in the file.
    Returns:
        Thhe number of characters in file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
