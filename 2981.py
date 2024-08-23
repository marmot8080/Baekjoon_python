def GCD(num, div):
    a = num
    b = div
    rest = a % b
    
    while rest != 0:
        a = b
        b = rest
        rest = a % b

    return b

if __name__ == '__main__':
    result = []

    n = int(input())
    num_arr = sorted(list(int(input()) for _ in range(n)))
    diff_arr = [num_arr[i] - num_arr[i-1] for i in range(1, n)]


    gcd = diff_arr[0]
    for i in range(1, n-1):
        gcd = GCD(gcd, diff_arr[i])
    
    for i in range(2, int(gcd**0.5) + 1):
        if gcd % i == 0:
            result.append(i)
            if i != gcd//i:
                result.append(gcd//i)
    result.append(gcd)

    for i in sorted(result):
        print(i, end=" ")