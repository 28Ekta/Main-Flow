# W6_Task:6- 
# Ques:39. Sudoku Validator

def is_valid_sudoku(board):
    for row in board:
        nums = [num for num in row if num != 0]
        if len(nums) != len(set(nums)):
            return False
    for col in range(9):
        nums = [board[row][col] for row in range(9) if board[row][col] != 0]
        if len(nums) != len(set(nums)):
            return False
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            nums = []
            for i in range(3):
                for j in range(3):
                    val = board[box_row + i][box_col + j]
                    if val != 0:
                        nums.append(val)
            if len(nums) != len(set(nums)):
                return False

    return True
board = [
 [5,3,0,0,7,0,0,0,0],
 [6,0,0,1,9,5,0,0,0],
 [0,9,8,0,0,0,0,6,0],
 [8,0,0,0,6,0,0,0,3],
 [4,0,0,8,0,3,0,0,1],
 [7,0,0,0,2,0,0,0,6],
 [0,6,0,0,0,0,2,8,0],
 [0,0,0,4,1,9,0,0,5],
 [0,0,0,0,8,0,0,7,9]
]
print(is_valid_sudoku(board))  


