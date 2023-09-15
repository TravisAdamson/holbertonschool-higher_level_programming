#!/usr/bin/python3
# 2-matrix_divided.py
# Travis Adamson
""" Defines a function that divides elements by given value """


def matrix_divided(matrix, div):
    """Returns the a new matrix.

    Float arguments will be typecasted to int before adding.

    Raises:
        TypeError: if values are not float or int
    """
    te_msg_a = "matrix must be a matrix (list of lists) of integers/floats"
    te_msg_b = "div must be a number"
    te_msg_c = "Each row of the matrix must have the same size"
    if type(div) != int and type(div) != float:
        raise TypeError(te_msg_b)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError(te_msg_a)
    if len(matrix) == 0:
        raise TypeError(te_msg_a)
    if type(matrix[0]) != list:
        raise TypeError(te_msg_a)
    m_len = len(matrix[0])
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(te_msg_a)
        if len(matrix[i]) != m_len:
            raise TypeError(te_msg_c)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError(te_msg_a)
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
