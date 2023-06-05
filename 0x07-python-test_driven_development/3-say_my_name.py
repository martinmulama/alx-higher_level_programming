#!/usr/bin/python3
"""
Module say_my_name
Prints a given first name and last name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first name> <last name>".

    Args:
        first_name: A string representing the first name.
        last_name: A string representing the last name. (Default: "")

    Raises:
        TypeError: If first_name is not a string or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = f"My name is {first_name} {last_name}"
    print(name)
