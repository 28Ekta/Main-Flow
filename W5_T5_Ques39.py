# W5_Task:5- 
# Ques:39. Sudoku Validator

def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue
            if num in rows[r] or num in cols[c] or num in boxes[(r//3)*3 + (c//3)]:
                return False
            rows[r].add(num)
            cols[c].add(num)
            boxes[(r//3)*3 + (c//3)].add(num)
    return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(board))
