left = [0, -1]
right = [0, 1]
up = [-1, 0]
down = [1, 0]

max = 0

def move_by_direction(count, board, direction):
    global max
    tmp_board = [row[:] for row in board]

    if direction[0] + direction[1] > 0:
        remove_blank_by_direction(tmp_board, direction)
        for i in range(n+1, 1, -1):
            for j in range(n+1, 1, -1):
                if tmp_board[i][j] == tmp_board[i - direction[0]][j - direction[1]]:
                    tmp_board[i][j] *= 2
                    tmp_board[i - direction[0]][j - direction[1]] = 0
        remove_blank_by_direction(tmp_board, direction)
    else:
        remove_blank_by_direction(tmp_board, direction)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if tmp_board[i][j] == 0:
                    for k in range(1, abs(i*direction[0] + j*direction[1]) - 1):
                        if tmp_board[i - k*direction[0]][j - k*direction[1]] != 0:
                            tmp_board[i][j] = tmp_board[i - k*direction[0]][j - k*direction[1]]
                            tmp_board[i - k*direction[0]][j - k*direction[1]] = 0
        remove_blank_by_direction(tmp_board, direction)
    if count == 4:
        for i in range(1, n+1):
            for j in range(1, n+1):
                if tmp_board[i][j] > max:
                    max = tmp_board[i][j]
    else:
        move_by_direction(count + 1, tmp_board, left)
        move_by_direction(count + 1, tmp_board, right)
        move_by_direction(count + 1, tmp_board, up)
        move_by_direction(count + 1, tmp_board, down)

def remove_blank_by_direction(board, direction):
    if direction[0] + direction[1] > 0:
        for i in range(n+1, 1, -1):
            for j in range(n+1, 1, -1):
                if board[i][j] == 0:
                    for k in range(1, abs(i*direction[0] + j*direction[1]) - 1):
                        if board[i - k*direction[0]][j - k*direction[1]] != 0:
                            board[i][j] = board[i - k*direction[0]][j - k*direction[1]]
                            board[i - k*direction[0]][j - k*direction[1]] = 0
    else:
        for i in range(1, n+1):
            for j in range(1, n+1):
                if board[i][j] == 0:
                    for k in range(1, abs(i*direction[0] + j*direction[1]) - 1):
                        if board[i - k*direction[0]][j - k*direction[1]] != 0:
                            board[i][j] = board[i - k*direction[0]][j - k*direction[1]]
                            board[i - k*direction[0]][j - k*direction[1]] = 0

def get_available_biggest_block(board):
    move_by_direction(0, board, left)
    move_by_direction(0, board, right)
    move_by_direction(0, board, up)
    move_by_direction(0, board, down)

if __name__ == '__main__':
    n = int(input())

    board = [[-1 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(1, n+1):
        row = [m for m in map(int, input().split())]
        for j in range(1, n+1):
            board[i][j] = row[j-1]

    get_available_biggest_block(board)

    print(max)