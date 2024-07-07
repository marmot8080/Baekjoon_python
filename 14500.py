import sys

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def DFS(row:int, column:int, sum:int = 0, count:int = 0):
    global board, visited, max_sum

    if count == 3:
        if max_sum < sum:
            max_sum = sum
        return
    
    for i in range(4):
        row_tmp = row + directions[i][0]
        column_tmp = column + directions[i][1]
        if 0 <= row_tmp < len(board) and 0<= column_tmp < len(board[0]) and not visited[row_tmp][column_tmp]:
            visited[row_tmp][column_tmp] = True
            DFS(row_tmp, column_tmp, sum + board[row_tmp][column_tmp], count+1)
            visited[row_tmp][column_tmp] = False

def T_shape(row, column):
    global board, max_sum

    if 0 < row < len(board) - 1 and 0 < column < len(board[0]) - 1:
        sum = board[row][column] + board[row-1][column] + board[row+1][column] + board[row][column-1] + board[row][column+1]
        sum -= min(board[row-1][column], board[row+1][column], board[row][column-1], board[row][column+1])
        if max_sum < sum:
            max_sum = sum
    else:
        for i in range(4):
            sum = board[row][column]
            for j in range(4):
                if i != j:
                    if 0 <= row + directions[j][0] < len(board) and 0<= column + directions[j][1] < len(board[0]):
                        sum += board[row + directions[j][0]][column + directions[j][1]]
                    else:
                        sum = 0
                        break
            if max_sum < sum:
                max_sum = sum

if __name__ == '__main__':
    global board, visited, max_sum
    board = []
    max_sum = 0
    row, column = map(int, sys.stdin.readline().split())
    visited = [[False for _ in range(column)] for _ in range(row)]

    for i in range(row):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(row):
        for j in range(i%2, column, 2):
            visited[i][j] = True
            DFS(i, j, board[i][j])
            visited[i][j] = False
        for j in range(column):
            T_shape(i, j)
    
    print(max_sum)