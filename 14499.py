import sys

east = 1
west = 2
north = 3
south = 4

dice = [[0, 0, 0] for _ in range(4)]

def dice_roller(board:list[list[int]], loc:list[int], direction:int):
    if direction == east:
        loc[1] += 1
        if loc[1] > len(board[loc[0]]) - 1:
            loc[1] -= 1
            return
        elif board[loc[0]][loc[1]] == 0:
            board[loc[0]][loc[1]] = dice[1][2]
            dice[1][2] = dice[3][1]
            dice[3][1] = dice[1][0]
            dice[1][0] = dice[1][1]
            dice[1][1] = board[loc[0]][loc[1]]
        else:
            dice[1][2] = dice[3][1]
            dice[3][1] = dice[1][0]
            dice[1][0] = dice[1][1]
            dice[1][1] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
    elif direction == west:
        loc[1] -= 1
        if loc[1] < 0:
            loc[1] += 1
            return
        elif board[loc[0]][loc[1]] == 0:
            board[loc[0]][loc[1]] = dice[1][0]
            dice[1][0] = dice[3][1]
            dice[3][1] = dice[1][2]
            dice[1][2] = dice[1][1]
            dice[1][1] = board[loc[0]][loc[1]]
        else:
            dice[1][0] = dice[3][1]
            dice[3][1] = dice[1][2]
            dice[1][2] = dice[1][1]
            dice[1][1] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
    elif direction == north:
        loc[0] -= 1
        if loc[0] < 0:
            loc[0] += 1
            return
        elif board[loc[0]][loc[1]] == 0:
            board[loc[0]][loc[1]] = dice[0][1]
            dice[0][1] = dice[3][1]
            dice[3][1] = dice[2][1]
            dice[2][1] = dice[1][1]
            dice[1][1] = board[loc[0]][loc[1]]
        else:
            dice[0][1] = dice[3][1]
            dice[3][1] = dice[2][1]
            dice[2][1] = dice[1][1]
            dice[1][1] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
    elif direction == south:
        loc[0] += 1
        if loc[0] > len(board) - 1:
            loc[0] -= 1
            return
        elif board[loc[0]][loc[1]] == 0:
            board[loc[0]][loc[1]] = dice[2][1]
            dice[2][1] = dice[3][1]
            dice[3][1] = dice[0][1]
            dice[0][1] = dice[1][1]
            dice[1][1] = board[loc[0]][loc[1]]
        else:
            dice[2][1] = dice[3][1]
            dice[3][1] = dice[0][1]
            dice[0][1] = dice[1][1]
            dice[1][1] = board[loc[0]][loc[1]]
            board[loc[0]][loc[1]] = 0
    else:
        print('Wrong command.')
        exit(0)

    print(dice[3][1])

if __name__ == '__main__':
    board = []
    loc = [0, 0]
    row, column, loc[0], loc[1], command_cnt = map(int, input().split())

    for i in range(row):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    direction = list(map(int, input().split()))

    for i in range(command_cnt):
        dice_roller(board, loc, direction[i])