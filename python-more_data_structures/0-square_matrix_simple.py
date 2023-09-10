#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append([])
        for i2 in i:
            new_matrix[i].append(i2 * i2)
    return new_matrix
