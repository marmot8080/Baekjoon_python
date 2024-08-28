from sys import stdin


if __name__ == '__main__':
    n, l = map(int, stdin.readline().split())
    height_map = []
    path_cnt = 0

    for _ in range(n):
        height_map.append([i for i in map(int, stdin.readline().split())])

    for i in range(n):
        tmp = height_map[i][0]
        count = 1
        flag = 1
        for j in range(1, n):
            if height_map[i][j] == tmp:
                count += 1
            elif height_map[i][j] == tmp + 1:
                if count < l:
                    flag = 0
                    break
                tmp = height_map[i][j]
                count = 1
            elif height_map[i][j] == tmp - 1:
                for k in range(l):
                    if j + k >= n or height_map[i][j+k] != tmp - 1:
                        flag = 0
                        break
                
                if not flag:
                    break
                else:
                    tmp -= 1
                    count = 1 - l
            else:
                flag = 0
                break
            
        if flag:
            path_cnt += 1

    for i in range(n):
        tmp = height_map[0][i]
        count = 1
        flag = 1
        for j in range(1, n):
            if height_map[j][i] == tmp:
                count += 1
            elif height_map[j][i] == tmp + 1:
                if count < l:
                    flag = 0
                    break
                tmp = height_map[j][i]
                count = 1
            elif height_map[j][i] == tmp - 1:
                for k in range(l):
                    if j + k >= n or height_map[j+k][i] != tmp - 1:
                        flag = 0
                        break
                
                if not flag:
                    break
                else:
                    tmp -= 1
                    count = 1 - l
            else:
                flag = 0
                break
            
        if flag:
            path_cnt += 1

    print(path_cnt)