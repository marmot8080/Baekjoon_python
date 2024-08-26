import sys

if __name__ == '__main__':
    n = int(input())
    x = [num for num in map(int, sys.stdin.readline().split())]
    sorted_x = sorted(x)
    result = []

    a = 0
    while a < n:
        result.append(sorted_x[a])
        a += sorted_x.count(sorted_x[a])
    
    for i in x:
        print(result.index(i), end=' ')