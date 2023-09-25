#!/usr/bin/python3
# 12-pascal_triangle.py
# Travis Adamson
""" Defines a function that returns a list of ints"""


def pascal_triangle(n):
    """Returns a list of ints representing pascal triangle of n.

    Args:
        n (int): The pascal triangle to rep.
    """
    if n <= 0:
        return []

    results = [[1]]
    while len(results) != n:
        tri = results[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        results.append(temp)
    return results
