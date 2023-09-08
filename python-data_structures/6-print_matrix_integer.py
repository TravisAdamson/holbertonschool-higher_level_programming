#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    toggle = 0
    for i in matrix:
        for j in i:
            if toggle != 0:
                print(" ", end="")
            print("{:d}".format(j), end="")
            toggle = 1
        print()
        toggle = 0
