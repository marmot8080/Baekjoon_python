min = 11
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def tilt_board(red_loc, blue_loc, direction, count):
    global min, directions

    count += 1

    if count > 10:
        pass
    else:
        red = red_loc.copy()
        blue = blue_loc.copy()

        while(board[red[0]][red[1]] != '#' and board[red[0]][red[1]] != 'O'):
            red[0] += direction[0]
            red[1] += direction[1]

        while(board[blue[0]][blue[1]] != '#' and board[blue[0]][blue[1]] != 'O'):
            blue[0] += direction[0]
            blue[1] += direction[1]
        
        if board[blue[0]][blue[1]] == 'O':
            pass
        elif board[red[0]][red[1]] == 'O' and count < min:
            min = count
        elif red == blue:
            red_tmp = list([red_loc[0] * direction[0], red_loc[1] * direction[1]])
            blue_tmp = list([blue_loc[0] * direction[0], blue_loc[1] * direction[1]])
            if red_tmp < blue_tmp:
                red[0] -= direction[0]
                red[1] -= direction[1]
            elif red_tmp > blue_tmp:
                blue[0] -= direction[0]
                blue[1] -= direction[1]
            
            red[0] -= direction[0]
            red[1] -= direction[1]
            blue[0] -= direction[0]
            blue[1] -= direction[1]
            
            if red == red_loc and blue == blue_loc:
                pass
            else:
                opposite_direction = list([direction[0] * -1, direction[1] * -1])
                for d in directions:
                    if d != direction and d != opposite_direction:
                        tilt_board(red, blue, d, count)
        else:
            red[0] -= direction[0]
            red[1] -= direction[1]
            blue[0] -= direction[0]
            blue[1] -= direction[1]

            if red == red_loc and blue == blue_loc:
                pass
            else:
                opposite_direction = list([direction[0] * -1, direction[1] * -1])
                for d in directions:
                    if d != direction and d != opposite_direction:
                        tilt_board(red, blue, d, count)

def get_least_movement(row, column):
    global directions

    for i in range(row):
        for j in range(column):
            if board[i][j] == 'R':
                red_loc = [i, j]
            elif board[i][j] == 'B':
                blue_loc = [i, j]
    
    for d in directions:
        tilt_board(red_loc, blue_loc, d, 0)

    if min > 10:
        return -1
    else:
        return min

row, column = map(int, input().split())
board = [list(input()) for _ in range(row)]

print(get_least_movement(row, column))
