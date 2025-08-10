# W5_Task:5- 
# Ques:38. Rotate Matrix 90° Clockwise

def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(mat))