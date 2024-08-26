from sys import stdin

if __name__ == '__main__':
    n = int(input())
    x = [num for num in map(int, stdin.readline().split())]
    sorted_x = sorted(set(x))
    dic = {sorted_x[i]: i for i in range(len(sorted_x))}

    for i in x:
        print(dic[i], end=' ')