#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    new_matrix = []
    
    for row in matrix:
        # Square each element in the row and append the new row to the new matrix
        new_matrix.append([x ** 2 for x in row])
    
    return new_matrix
