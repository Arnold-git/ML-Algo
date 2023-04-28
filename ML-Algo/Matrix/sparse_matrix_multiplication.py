

def sparse_matrix_multiplication(matrix_a, matrix_b):

    """
     Function to multiply two integer matrix
    """
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    
    sparse_a = get_dict_of_nonzero_cell(matrix_a)
    sparse_b = get_dict_of_nonzero_cell(matrix_b)

    matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i, k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b.keys():
                matrix_c[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]
    return matrix_c
    

def get_dict_of_nonzero_cell(matrix):
    dict_of_nonzero_cells = {}
    for rows in range(len(matrix)):
        for columns in range(len(matrix[0])):
            if matrix[rows][columns] != 0:
                
                dict_of_nonzero_cells[(rows, columns)] = matrix[rows][columns]


    return dict_of_nonzero_cells


if __name__ == "__main__":
 
 
 matrix_a = [
    [0, 2, 0],
    [0, -3, 5]
]

matrix_b = [
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 4]
]

print(sparse_matrix_multiplication(matrix_a, matrix_b))