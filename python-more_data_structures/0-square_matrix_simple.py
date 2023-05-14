#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_reloaded = []
    for i in matrix:
         matrix_reloaded.append(list(map(lambda x: x**2, i)))
    return (matrix_reloaded)
