import math

# Initial empty board
board = [" " for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def check_winner(bd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(bd[i] == player for i in condition) for condition in win_conditions)

def is_draw(bd):
    return " " not in bd and not check_winner(bd, "X") and not check_winner(bd, "O")

def minimax(bd, depth, is_maximizing):
    if check_winner(bd, "O"):
        return 1
    elif check_winner(bd, "X"):
        return -1
    elif is_draw(bd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if bd[i] == " ":
                bd[i] = "O"
                score = minimax(bd, depth + 1, False)
                bd[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if bd[i] == " ":
                bd[i] = "X"
                score = minimax(bd, depth + 1, True)
                bd[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Welcome to Tic Tac Toe (You are X, AI is O)")
    print_board()

    while True:
        # Player's move
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI is thinking...")
        ai_move = best_move()
        board[ai_move] = "O"
        print_board()

        if check_winner(board, "O"):
            print("AI wins! 🤖")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Run the game
play_game()
