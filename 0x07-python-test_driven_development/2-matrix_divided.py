#!/usr/bin/python3
"""Module for matrix division function

    Function: matrix_divided(matrix, div)

    return: list of each member of matrix by div
"""

def matrix_divided(matrix, div):
    """Compute and return the division of matrix members by div.
    
    Examples:
        >>>matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ...]
        ...matrix_divided(matrix, 3)    
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    Args:
        matrix (list): A list representing the first arg.
        div (int): A number representing the secound arg.
    returns:
        List: new list of matrix members divided by div
    """
    new_list = []
    temp_list = []
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    items_length = len(matrix[0])
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for item in matrix:
        if type(item) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(item) != items_length:
            raise TypeError("Each row of the matrix must have the same size")
        
        i = 0
        while i < len(item):
            temp_list.append(round((item[i]/div), 2))
            i += 1
        
        new_list.append(temp_list.copy())
        temp = []
    
    return new_list
