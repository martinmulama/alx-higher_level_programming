#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats. Each row of the matrix
                should have the same size.
        div: A number (integer or float) to divide the elements of the matrix by.
             Must not be equal to 0.

    Returns:
        A new matrix where all elements have been divided by div and rounded to
        2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
