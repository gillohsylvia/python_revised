
"""
* given a matrix
* perform a nested loop
* print the elements with a string format
"""

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end='')
                #print(matrix[i][j], end='')
                if j + 1 < len(matrix[0]):
                    print(' ', end='')
            print()
