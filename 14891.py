def rotate(gear_num, direction):
    post_num = gear[gear_num][0]
    for i in range(8 + direction, 8 + 8*direction, direction):
        tmp = gear[gear_num][i%8]
        gear[gear_num][i%8] = post_num
        post_num = tmp
    gear[gear_num][0] = post_num

    if gear_num - 1 >= 0 and rotated_gear[gear_num - 1] == 0 and  gear[gear_num][6+direction] != gear[gear_num-1][2]:
        rotated_gear[gear_num - 1] = 1
        rotate(gear_num-1, -1 * direction)
    
    if gear_num + 1 < 4 and rotated_gear[gear_num + 1] == 0 and  gear[gear_num][2+direction] != gear[gear_num+1][6]:
        rotated_gear[gear_num + 1] = 1
        rotate(gear_num+1, -1 * direction)


if __name__ == '__main__':
    gear = []
    for _ in range(4):
        gear.append(list(map(int, input())))
    k = int(input())

    for _ in range(k):
        rotated_gear = [0 for _ in range(4)]
        gear_num, direction = map(int, input().split())

        rotated_gear[gear_num-1] = 1
        rotate(gear_num-1, direction)
    
    score = gear[0][0] + 2*gear[1][0] + 4*gear[2][0] + 8*gear[3][0]

    print(score)