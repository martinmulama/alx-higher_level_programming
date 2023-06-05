#!/usr/bin/python3
"""
Module say_my_name
Prints a given first name and last name.
"""

def print_square(size):
    """
    Prints a square of a given size using the character "#".

    Args:
        size: An integer representing the size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
