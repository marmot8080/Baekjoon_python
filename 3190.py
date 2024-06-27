class body_queue():
    __queue = []
    __MAX_SIZE = 10000

    def __init__(self, start_loc: list = [0, 0]):
        self.__queue.append(start_loc[:])
        self.__head = 0
        self.__tail = -1

    def enqueue(self, head: list):
        self.__head += 1
        if self.__head < self.__MAX_SIZE:
            self.__queue.append(head[:])
        else:
            self.__queue[self.__head % self.__MAX_SIZE] = head[:]

    def dequeue(self):
        if self.__tail < self.__head:
            self.__tail += 1
            return self.__queue[self.__tail]
    
    def collision_with_myself(self, head: list):
        if self.__tail > 0 and self.__tail < self.__head:
            for i in range(self.__tail + 1, self.__head + 1):
                if self.__queue[i % self.__MAX_SIZE] == head:
                    return True
        return False

def turn_right(direction: list):
    return [direction[1], direction[0] * -1]

def turn_left(direction: list):
    return [direction[1] * -1, direction[0]]

def get_end_time(board_size: int, apple_loc: list, moves: list, start_direction: list = [0, 1]):
    direction = start_direction
    time_count = 0
    body = body_queue()
    head = [0, 0]
    turn_count = 0
    
    while head[0] in range(0, board_size) and head[1] in range(0, board_size):
        time_count += 1
        head[0] += direction[0]
        head[1] += direction[1]
        
        if body.collision_with_myself(head):
            return time_count
        else:
            body.enqueue(head)

        if head in apple_loc:
            apple_loc.remove(head)
        else:
            body.dequeue()
        
        if turn_count < len(moves) and time_count == moves[turn_count][0]:
            if moves[turn_count][1] == 'L':
                direction = turn_left(direction)
                turn_count += 1
            elif moves[turn_count][1] == 'D':
                direction = turn_right(direction)
                turn_count += 1
            else:
                print('잘못된 방향의 입력입니다.')
                return time_count
    
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