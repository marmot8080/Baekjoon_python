import sys
import copy

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def build_wall(start, count):
    if count == 3:
        lab_tmp = copy.deepcopy(lab)
        
        for virus in virus_loc:
            spread_virus(virus[0], virus[1], lab_tmp)

        safe_areas(lab_tmp)
    else:
        for i in range(start + 1, len(empty_space)):
            lab[empty_space[i][0]][empty_space[i][1]] = 1
            build_wall(i, count+1)
            lab[empty_space[i][0]][empty_space[i][1]] = 0

def spread_virus(x, y, lab_tmp):
    for direction in directions:
        x_tmp = x + direction[0]
        y_tmp = y + direction[1]
        if 0 <= x_tmp < row and 0 <= y_tmp < column and lab_tmp[x_tmp][y_tmp] == 0:
            lab_tmp[x_tmp][y_tmp] = 2
            spread_virus(x_tmp, y_tmp, lab_tmp)

def safe_areas(lab_tmp):
    global result
    count = 0

    for i in range(row):
        count += lab_tmp[i].count(0)

    result = max(result, count)

def max_safe_area():
    for i in range(len(empty_space)):
        lab[empty_space[i][0]][empty_space[i][1]] = 1
        build_wall(i, 1)
        lab[empty_space[i][0]][empty_space[i][1]] = 0

if __name__ == '__main__':
    global row, column, result
    result = 0
    row, column = map(int, input().split())
    lab = []
    empty_space = []
    virus_loc = []

    for _ in range(row):
        lab.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(row):
        for j in range(column):
            if lab[i][j] == 0:
                empty_space.append([i, j])
            elif lab[i][j] == 2:
                virus_loc.append([i, j])

    max_safe_area()

    print(result)