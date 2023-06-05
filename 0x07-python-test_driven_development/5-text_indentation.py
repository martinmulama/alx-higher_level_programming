#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each ".", "?", and ":" character.

    Args:
        text: A string representing the input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = (".", "?", ":")
    result = ""
    for char in text:
        result += char
        if char in punctuation:
            result += "\n\n"
    print(result.strip())
