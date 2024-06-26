left = [0, -1]
right = [0, 1]
up = [-1, 0]
down = [1, 0]

max_block = 0

def move_by_direction(board, size, direction, count):
    global max_block
    tmp_board = [row[:] for row in board]

    # TODO: remove_blank_by_direction()의 반복문 형태로 블록 합치기 실행
    # --> 합쳐진 이후 역순의 반복문을 통해 공백을 탐색하여 공백 제거
    # (함수 호출 감소로 인한 실행시간 단축 기대 but 가독성 저하될 가능성 우려)
    if direction[0] + direction[1] > 0:
        remove_blank_by_direction(tmp_board, size, direction)
        for i in range(size, direction[0], -1):
            for j in range(size, direction[1], -1):
                if tmp_board[i][j] == tmp_board[i - direction[0]][j - direction[1]]:
                    tmp_board[i][j] *= 2
                    tmp_board[i - direction[0]][j - direction[1]] = 0
        remove_blank_by_direction(tmp_board, size, direction)
    else:
        remove_blank_by_direction(tmp_board, size, direction)
        for i in range(1, size + 1 + direction[0]):
            for j in range(1, size + 1 + direction[1]):
                if tmp_board[i][j] == tmp_board[i - direction[0]][j - direction[1]]:
                    tmp_board[i][j] *= 2
                    tmp_board[i - direction[0]][j - direction[1]] = 0
        remove_blank_by_direction(tmp_board, size, direction)

    if count == 4:
        max_block = max(max_block, max(max(tmp_board)))
    else:
        move_by_direction(tmp_board, size, left, count + 1)
        move_by_direction(tmp_board, size, right, count + 1)
        move_by_direction(tmp_board, size, up, count + 1)
        move_by_direction(tmp_board, size, down, count + 1)

def remove_blank_by_direction(board, size, direction):
    if direction[0] + direction[1] > 0:
        for i in range(size, 0, -1):
            for j in range(size, 0, -1):
                if board[i][j] == 0:
                    for k in range(1, abs(i*direction[0] + j*direction[1])):
                        if board[i - k*direction[0]][j - k*direction[1]] != 0:
                            board[i][j] = board[i - k*direction[0]][j - k*direction[1]]
                            board[i - k*direction[0]][j - k*direction[1]] = 0
                            break
    else:
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                if board[i][j] == 0:
                    for k in range(1, size + 1 - abs(i*direction[0] + j*direction[1])):
                        if board[i - k*direction[0]][j - k*direction[1]] != 0:
                            board[i][j] = board[i - k*direction[0]][j - k*direction[1]]
                            board[i - k*direction[0]][j - k*direction[1]] = 0
                            break

if __name__ == '__main__':
    n = int(input())

    board = [[-1 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(1, n+1):
        row = [m for m in map(int, input().split())]
        for j in range(1, n+1):
            board[i][j] = row[j-1]

    move_by_direction(board, n, left, 0)
    move_by_direction(board, n, right, 0)
    move_by_direction(board, n, up, 0)
    move_by_direction(board, n, down, 0)

    print(max_block)