#!/usr/bin/python3
"""Module for add_integer method"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: An integer or float, the first number to be added.
        b: An integer or float, the second number to be added. (Default: 98)

    Returns:
        An integer, the sum of a and b.

    Raises:
        TypeError: If a is not an integer or float.
        TypeError: If b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
