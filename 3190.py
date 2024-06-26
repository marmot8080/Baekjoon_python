start_direction = [0, 1]

def turn_right(direction):
    return [direction[1], direction[0] * -1]

def turn_left(direction):
    return [direction[1] * -1, direction[0]]

# 몸 길이가 2 이상일 때 방향 전환 등의 상황에서 어떻게 처리해야하는지(사과의 의미가 무엇인지)
# n초 뒤 방향 전환을 할 경우 1칸을 이동하고 전환하는지, 전환하고 이동하는지, 전환만 하는지
# 위의 전제들에 대해 확인해 볼 필요가 있음
def get_end_time(board_size, apple_locations, moves):
    apple_count = len(apple_locations)
    direction = start_direction
    row = 0
    column = 0
    time_count = 0
    body_length = 1
    
    for i in range(len(moves)):
        tmp = row*abs(direction[0]) + column*abs(direction[1]) + moves[i][0]*(direction[0]+direction[1])
        if tmp < 0 or tmp >= board_size:
            pass
        else:
            pass
    
    return time_count

if __name__ == '__main__':
    board_size = int(input())

    apple_count = int(input())
    apple_locations = []
    for i in range(apple_count):
        apple_locations.append([m for m in map(int, input().split())])
    
    move_count = int(input())
    moves = []
    for i in range(move_count):
        move, direction = input().split()
        move = int(move)
        moves.append([move, direction])
    
    print(get_end_time(board_size, apple_locations, moves))