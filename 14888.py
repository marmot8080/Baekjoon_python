def calculate(result):
    global max_result, min_result, flag

    if sum(operator_cnt) - sum(used_operator_cnt) == 0:
        if flag == 0:
            flag = 1
            max_result = result
            min_result = result
        else:
            max_result = max(max_result, result)
            min_result = min(min_result, result)
    else:
        for i in range(4):
            if operator_cnt[i] - used_operator_cnt[i] > 0:
                used_operator_cnt[i] += 1
                idx = sum(used_operator_cnt)
                if i == 0:
                    calculate(result + num_arr[idx])
                elif i == 1:
                    calculate(result - num_arr[idx])
                elif i == 2:
                    calculate(result * num_arr[idx])
                elif i == 3:
                    if result < 0:
                        calculate(-1 * ((-1 * result) // num_arr[idx]))
                    else:
                        calculate(result // num_arr[idx])
                used_operator_cnt[i] -= 1

if __name__ == '__main__':
    flag = 0
    max_result = 0
    min_result = 0
    num_cnt = int(input())
    num_arr = [i for i in map(int, input().split())]

    # 0: +, 1: -, 2: *, 3: /
    operator_cnt = [i for i in map(int, input().split())]

    for i in range(4):
        if operator_cnt[i] > 0:
            used_operator_cnt = [0 for _ in range(4)]
            used_operator_cnt[i] += 1
            if i == 0:
                calculate(num_arr[0] + num_arr[1])
            elif i == 1:
                calculate(num_arr[0] - num_arr[1])
            elif i == 2:
                calculate(num_arr[0] * num_arr[1])
            elif i == 3:
                calculate(num_arr[0] // num_arr[1])
            used_operator_cnt[i] -= 1
    
    print(max_result)
    print(min_result)