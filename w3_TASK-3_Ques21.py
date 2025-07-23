# 21. Matrix Addition

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
print(add_matrices(m1, m2)) 