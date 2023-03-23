#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the first row of the triangle
    row = [1]

    # Initialize the triangle with the first row
    triangle = [row]

    # Generate the remaining rows of the triangle
    for i in range(1, n):
        # Generate the next row by adding adjacent elements of the previous row
        row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
        # Append the row to the triangle
        triangle.append(row)
    return triangle
