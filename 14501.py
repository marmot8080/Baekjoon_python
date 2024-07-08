import sys

def get_max_profit(count, time_taken, cost):
    pass

if __name__ == '__main__':
    count = int(input())
    time_taken = [0 for _ in range(count)]
    cost = [0 for _ in range(count)]

    for i in range(count):
        time_taken[i], cost[i] = map(int, sys.stdin.readlie().split())
    
