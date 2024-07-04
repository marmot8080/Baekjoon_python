import sys
import copy

def get_max_sum(row:int, column:int, visited:list[list[int]], candidate:list[list[int]]=[], count:int = 0):
    global max_sum
    global board
    
    if count == 3:
        sum = 0
        for i in range(4):
            sum += board[visited[i][0]][visited[i][1]]
        
        if max_sum < sum:
            max_sum = sum
    else:
        candidate_tmp = [loc.copy() for loc in candidate if loc != [row, column]]

        if row+1 < len(board) and not [row+1, column] in visited:
            candidate_tmp.append([row+1, column])
        if row-1 < len(board) and not [row-1, column] in visited:
            candidate_tmp.append([row-1, column])
        if column+1 < len(board[0]) and not [row, column+1] in visited:
            candidate_tmp.append([row, column+1])
        if column-1 >= 0 and not [row, column-1] in visited:
            candidate_tmp.append([row, column-1])

        for loc in candidate_tmp:
            visited_tmp = copy.deepcopy(visited)
            visited_tmp.append(loc)
            get_max_sum(loc[0], loc[1], visited_tmp, candidate_tmp, count+1)

if __name__ == '__main__':
    global board
    global max_sum
    board = []
    max_sum = 0
    row, column = map(int, sys.stdin.readline().split())

    for i in range(row):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(row):
        for j in range(i%2, column, 2):
            get_max_sum(i, j, [[i, j]])
    
    print(max_sum)