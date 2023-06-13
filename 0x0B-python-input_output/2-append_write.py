#!/usr/bin/python3
# 2-append_write.py
# Martin <martin.mulama@yahoo.com>
""" Module that appends a string to a tct file and returns no of characters written """

def append_write(filename="", text=""):
    """appends a string to a text file (UTF8) and returns the number of characters written.
    Args:
        filename="": The name of file to open.
        text="": The text write in the file.
    Returns:
        The number of characters in file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
