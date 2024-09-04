from sys import stdin


dx = [-1, 0, 1, 0, -1, 0, 1, 0]
dy = [0, 1, 0, -1, 0, 1, 0, -1]


def CCTV(cctv, office):
    global n, m, cctv_cnt, min_blind_spot

    if cctv == cctv_cnt:
        blind_spot = 0
        for i in range(n):
            blind_spot += office[i].count(0)
        min_blind_spot = min(blind_spot, min_blind_spot)
    else:
        x = cctv_loc[cctv][0]
        y = cctv_loc[cctv][1]
        if office[x][y] == 1:
            for k in range(4):
                office_tmp = [[j for j in office[i]] for i in range(n)]
                l = 1
                while 0 <= x + l*dx[k] < n and 0 <= y + l*dy[k] < m:
                    if office_tmp[x + l*dx[k]][y + l*dy[k]] in (0, '#'):
                        office_tmp[x + l*dx[k]][y + l*dy[k]] = '#'
                        l += 1
                    else:
                        break
                CCTV(cctv + 1, office_tmp)
        elif office[x][y] == 2:
            for k in range(2):
                office_tmp = [[j for j in office[i]] for i in range(n)]
                l = 1
                while 0 <= x + l*dx[k] < n and 0 <= y + l*dy[k] < m:
                    if office_tmp[x + l*dx[k]][y + l*dy[k]] in (0, '#'):
                        office_tmp[x + l*dx[k]][y + l*dy[k]] = '#'
                        l += 1
                    else:
                        break
                l = 1
                while 0 <= x - l*dx[k] < n and 0 <= y - l*dy[k] < m:
                    if office_tmp[x - l*dx[k]][y - l*dy[k]] in (0, '#'):
                        office_tmp[x - l*dx[k]][y - l*dy[k]] = '#'
                        l += 1
                    else:
                        break
                CCTV(cctv + 1, office_tmp)
        elif office[x][y] == 3:
            for k in range(4):
                office_tmp = [[j for j in office[i]] for i in range(n)]
                for a in range(k, k+2):
                    l = 1
                    while 0 <= x + l*dx[a] < n and 0 <= y + l*dy[a] < m:
                        if office_tmp[x + l*dx[a]][y + l*dy[a]] in (0, '#'):
                            office_tmp[x + l*dx[a]][y + l*dy[a]] = '#'
                            l += 1
                        else:
                            break
                CCTV(cctv + 1, office_tmp)
        elif office[x][y] == 4:
            for k in range(4):
                office_tmp = [[j for j in office[i]] for i in range(n)]
                for a in range(k, k+3):
                    l = 1
                    while 0 <= x + l*dx[a] < n and 0 <= y + l*dy[a] < m:
                        if office_tmp[x + l*dx[a]][y + l*dy[a]] in (0, '#'):
                            office_tmp[x + l*dx[a]][y + l*dy[a]] = '#'
                            l += 1
                        else:
                            break
                CCTV(cctv + 1, office_tmp)
        elif office[x][y] == 5:
            office_tmp = [[j for j in office[i]] for i in range(n)]
            for k in range(4):
                l = 1
                while 0 <= x + l*dx[k] < n and 0 <= y + l*dy[k] < m:
                    if office_tmp[x + l*dx[k]][y + l*dy[k]] in (0, '#'):
                        office_tmp[x + l*dx[k]][y + l*dy[k]] = '#'
                        l += 1
                    else:
                        break
            CCTV(cctv + 1, office_tmp)


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    min_blind_spot = n*m
    office = []
    for _ in range(n):
        office.append(list(map(int, stdin.readline().split())))
    cctv_loc = []
    for i in range(n):
        for j in range(m):
            if 0 < office[i][j] <= 5:
                cctv_loc.append([i, j])
    cctv_cnt = len(cctv_loc)
    
    CCTV(0, office)

    print(min_blind_spot)
