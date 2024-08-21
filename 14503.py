import sys

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def clean_room(direction):
    global count

    if room[loc[0]][loc[1]] == 0:
        count += 1
        room[loc[0]][loc[1]] = 2
    
    for _ in range(4):
        direction = (direction + 1) % 4
        if room[loc[0] + dx[direction]][loc[1] + dy[direction]] == 0:
            loc[0] += dx[direction]
            loc[1] += dy[direction]
            clean_room(direction)
            return
    
    if room[loc[0] - dx[direction]][loc[1] - dy[direction]] == 2:
        loc[0] -= dx[direction]
        loc[1] -= dy[direction]
        clean_room(direction)

if __name__ == '__main__':
    loc = [0, 0]
    room = []
    count = 0
    n, m = map(int, input().split())
    loc[0], loc[1], direction = map(int, input().split())
    direction = 3 - direction

    for i in range(n):
        room.append(list(map(int, sys.stdin.readline().split())))

    clean_room(direction)

    print(count)