def solve_board(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(board, i, (row,col)):
            board[row][col] = i

            if solve_board(board):
                return True

            board[row][col] = 0

    return False


def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check square
    x_start = pos[1] // 3
    y_start = pos[0] // 3

    for i in range(y_start*3, y_start*3+3):
        for j in range(x_start*3, x_start*3+3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True 


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) # row, col
    return None
