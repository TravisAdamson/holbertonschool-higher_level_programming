#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for i2 in matrix[i]:
            new_matrix[i].append(i2 * i2)
    return new_matrix
