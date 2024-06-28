def get_min_inspector_count(candidate_cnt: list, general_cap: int, deputy_cap: int):
    count = 0

    for i in range(len(candidate_cnt)):
        count += 1
        if candidate_cnt[i] > general_cap:
            candidate_cnt[i] -= general_cap
            count += int(candidate_cnt[i] / deputy_cap)
            if candidate_cnt[i] % deputy_cap > 0:
                count += 1
    
    return count

if __name__ == '__main__':
    center_cnt = int(input())
    candidate_cnt = [n for n in map(int, input().split())]
    
    general_cap, deputy_cap = map(int, input().split())

    print(get_min_inspector_count(candidate_cnt, general_cap, deputy_cap))