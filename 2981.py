if __name__ == '__main__':
    num_arr = []
    tmp_arr = []
    result = []

    n = int(input())
    min_num = int(input())
    num_arr.append(min_num)

    for i in range(n-1):
        num_arr.append(int(input()))
    
    for i in range(min_num - 1):
        tmp_arr.clear()
        tmp_arr = [num - i for num in num_arr]
        
        for j in range(2, min_num + 1):
            tmp = 0
            for k in range(n):
                if not tmp_arr[k] % j == 0:
                    tmp = 1
                    break
            if tmp == 0 and not j in result:
                result.append(j)
    
    result.sort()

    for i in range(len(result)):
        print(result[i], end=" ")