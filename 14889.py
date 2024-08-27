from sys import stdin


def get_min_diff(count, start, sum):
    global n, min
    
    if count == n/2:
        if abs(2 * sum - total) // 2 < min:
            min = abs(2 * sum - total) // 2
    else:
        for i in range(start, n):
            get_min_diff(count+1, i+1, sum+synergy_sum[i])


if __name__ == '__main__':
    n = int(input())
    synergy = []
    synergy_sum = []

    for _ in range(n):
        synergy.append(list(map(int, stdin.readline().split())))
    
    for i in range(n):
        tmp = sum(synergy[i])
        for j in range(n):
            tmp += synergy[j][i]
        synergy_sum.append(tmp)
    
    total = sum(synergy_sum)
    min = total

    for i in range(n):
        get_min_diff(1, i+1, synergy_sum[i])

    print(min)