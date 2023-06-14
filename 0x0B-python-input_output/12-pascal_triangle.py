#!/usr/bin/python3

"""
A module that represents Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.
    """
    pascal = []
    if type(n) != int:
        raise TypeError("n must be an integer")
    elif n <= 0:
        return pascal
    else:
        pascal = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                content = pascal[i - 1][j - 1] + pascal[i - 1][j]
                row.append(content)
            row.append(1)
            pascal.append(row)
        return pascal
