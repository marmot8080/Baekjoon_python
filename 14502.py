import sys
import copy

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def build_wall(x, y, count):
    if count == 3:
        lab_tmp = copy.deepcopy(lab)
        virus_loc = []

        for i in range(row):
            for j in range(column):
                if lab_tmp[i][j] == 2:
                    virus_loc.append([i, j])
        
        for virus in virus_loc:
            spread_virus(virus[0], virus[1], lab_tmp)

        safe_areas(lab_tmp)

        del lab_tmp
    else:
        tmp = 0
        for i in range(row):
            for j in range(column):
                if tmp == 0:
                    tmp = 1
                    i = x
                    j = y
                    continue
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    build_wall(i, j, count+1)
                    lab[i][j] = 0

def spread_virus(x, y, lab_tmp):
    for direction in directions:
        x_tmp = x + direction[0]
        y_tmp = y + direction[1]
        if 0 <= x_tmp < row and 0 <= y_tmp < column and lab_tmp[x_tmp][y_tmp] == 0:
            lab_tmp[x_tmp][y_tmp] = 2
            spread_virus(x_tmp, y_tmp, lab_tmp)

def safe_areas(lab_tmp):
    global max
    count = 0

    for i in range(row):
        for j in range(column):
            if lab_tmp[i][j] == 0:
                count += 1

    if count > max:
        max = count

def max_safe_area():
    for i in range(row):
        for j in range(column):
            if lab[i][j] == 0:
                lab[i][j] = 1
                build_wall(i, j, 1)
                lab[i][j] = 0

if __name__ == '__main__':
    global row, column, max
    max = 0
    row, column = map(int, input().split())
    lab = []

    for _ in range(row):
        lab.append(list(map(int, sys.stdin.readline().split())))

    max_safe_area()

    print(max)