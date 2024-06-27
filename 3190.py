start_direction = [0, 1]

class body_queue():
    __queue = []
    __head = 0
    __tail = 0
    __MAX_SIZE = 10000

    def __init__(self, start_loc):
        self.__queue.append(start_loc)

    def enqueue(self, head):
        if not head in self.__queue:
            self.__queue[self.__tail % self.__MAX_SIZE] = head
            self.__tail += 1

    def dequeue(self):
        if self.__head > self.__tail:
            loc = self.__queue[self.__head]
            self.__head += 1
            return loc

def turn_right(direction):
    return [direction[1], direction[0] * -1]

def turn_left(direction):
    return [direction[1] * -1, direction[0]]

def get_end_time(board_size, apple_loc, moves):
    direction = start_direction
    row = 0
    column = 0
    time_count = 0
    body = body_queue([0, 0])
    
    for i in range(len(moves)):
        tmp = row*abs(direction[0]) + column*abs(direction[1]) + moves[i][0]*(direction[0]+direction[1])
        if tmp < 0 or tmp >= board_size:
            # 몇 번 더 움직이고 끝나는지 계산하여 종료시간 반환
            pass
        else:
            # 방향에 따라 head 위치 설정
            # head의 위치가 apple_loc에 포함되지 않을 경우 dequeue
            # head 위치 enqueue
            # moves[i][1]이 'L'일 경우 direction = turn_left(direction), 
            # 'D'일 경우 direction = turn_right(direction)
            pass
    
    return time_count

if __name__ == '__main__':
    board_size = int(input())

    apple_count = int(input())
    apple_loc = []
    for i in range(apple_count):
        apple_loc.append([m-1 for m in map(int, input().split())])
    
    move_count = int(input())
    moves = []
    for i in range(move_count):
        move, direction = input().split()
        move = int(move)
        moves.append([move, direction])
    
    print(get_end_time(board_size, apple_loc, moves))