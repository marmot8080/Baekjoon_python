def tilt_right(Rx, Ry, Bx, By, count):
    global min
    count += 1

    if count > 10:
        pass
    else:
        rx = Rx
        ry = Ry
        bx = Bx
        by = By

        while(board[rx][ry + 1] != '#' and board[rx][ry + 1] != 'O'):
            ry += 1

        while(board[bx][by + 1] != '#' and board[bx][by + 1] != 'O'):
            by += 1
        
        if board[bx][by + 1] == 'O':
            pass
        elif board[rx][ry + 1] == 'O' and count < min:
            min = count
        elif rx == bx and ry == by:
            if Ry > By:
                by -= 1
            else:
                ry -= 1
            
            tilt_right(rx, ry, bx, by, count)
            tilt_backward(rx, ry, bx, by, count)
            tilt_forward(rx, ry, bx, by, count)
        else:
            tilt_right(rx, ry, bx, by, count)
            tilt_backward(rx, ry, bx, by, count)
            tilt_forward(rx, ry, bx, by, count)

def tilt_left(Rx, Ry, Bx, By, count):
    global min
    count += 1

    if count > 10:
        pass
    else:
        rx = Rx
        ry = Ry
        bx = Bx
        by = By

        while(board[rx][ry - 1] != '#' and board[rx][ry - 1] != 'O'):
            ry -= 1

        while(board[bx][by - 1] != '#' and board[bx][by - 1] != 'O'):
            by -= 1
        
        if board[bx][by - 1] == 'O':
            pass
        elif board[rx][ry - 1] == 'O' and count < min:
            min = count
        elif rx == bx and ry == by:
            if Ry > By:
                ry += 1
            else:
                by += 1
            
            tilt_left(rx, ry, bx, by, count)
            tilt_backward(rx, ry, bx, by, count)
            tilt_forward(rx, ry, bx, by, count)
        else:
            tilt_left(rx, ry, bx, by, count)
            tilt_backward(rx, ry, bx, by, count)
            tilt_forward(rx, ry, bx, by, count)

def tilt_backward(Rx, Ry, Bx, By, count):
    global min
    count += 1

    if count > 10:
        pass
    else:
        rx = Rx
        ry = Ry
        bx = Bx
        by = By

        while(board[rx + 1][ry] != '#' and board[rx + 1][ry] != 'O'):
            rx += 1

        while(board[bx + 1][by] != '#' and board[bx + 1][by] != 'O'):
            bx += 1
        
        if board[bx + 1][by] == 'O':
            pass
        elif board[rx + 1][ry] == 'O' and count < min:
            min = count
        elif rx == bx and ry == by:
            if Rx > Bx:
                bx -= 1
            else:
                rx -= 1
            
            tilt_right(rx, ry, bx, by, count)
            tilt_left(rx, ry, bx, by, count)
            tilt_backward(rx, ry, bx, by, count)
        else:
            tilt_right(rx, ry, bx, by, count)
            tilt_left(rx, ry, bx, by, count)
            tilt_backward(rx, ry, bx, by, count)

def tilt_forward(Rx, Ry, Bx, By, count):
    global min
    count += 1

    if count > 10:
        pass
    else:
        rx = Rx
        ry = Ry
        bx = Bx
        by = By

        while(board[rx - 1][ry] != '#' and board[rx - 1][ry] != 'O'):
            rx -= 1

        while(board[bx - 1][by] != '#' and board[bx - 1][by] != 'O'):
            bx -= 1
        
        if board[bx - 1][by] == 'O':
            pass
        elif board[rx - 1][ry] == 'O' and count < min:
            min = count
        elif rx == bx and ry == by:
            if Rx > Bx:
                rx += 1
            else:
                bx += 1
            
            tilt_right(rx, ry, bx, by, count)
            tilt_left(rx, ry, bx, by, count)
            tilt_forward(rx, ry, bx, by, count)
        else:
            tilt_right(rx, ry, bx, by, count)
            tilt_left(rx, ry, bx, by, count)
            tilt_forward(rx, ry, bx, by, count)

def get_least_movement(column, row):
    global min

    for i in range(row):
        for j in range(column):
            if board[i][j] == 'R':
                Rx = i
                Ry = j
            elif board[i][j] == 'B':
                Bx = i
                By = j
    
    tilt_right(Rx, Ry, Bx, By, 0)
    tilt_left(Rx, Ry, Bx, By, 0)
    tilt_backward(Rx, Ry, Bx, By, 0)
    tilt_forward(Rx, Ry, Bx, By, 0)

    if min > 10:
        return -1
    else:
        return min

if __name__ == '__main__':
    global board, min
    min = 11
    row, column = map(int, input().split())
    board = [list(input()) for _ in range(row)]

    print(get_least_movement(column, row))
