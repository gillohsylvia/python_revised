"""
* given a matrix
* loop through the elements of the matrix
* multiply ach element of the loop by itself
* append the results to a new_matrix
* return the new_matrix
"""
def square_matrix_simple(matrix=[]):
    #new_matrix = [[x**2 for x in y]for y in matrix]
    new_matrix = []
    for y in matrix:
        temp = []
        for x in y:
            temp.append(x**2)
        new_matrix.append(temp)
    return new_matrix
           
