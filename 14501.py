import sys

def max_profit(n, sum):
    global count, max_sum

    if n >= count:
        if sum > max_sum:
            max_sum = sum
        return

    max_profit(n + 1, sum)
    if n + time_taken[n] <= count:
        max_profit(n + time_taken[n], sum + cost[n])

if __name__ == '__main__':
    global count, max_sum
    
    max_sum = 0
    count = int(input())
    time_taken = [0 for _ in range(count)]
    cost = [0 for _ in range(count)]

    for i in range(count):
        time_taken[i], cost[i] = map(int, sys.stdin.readline().split())
    
    max_profit(0, 0)

    print(max_sum)