import sys
sys.stdin = open('../INPUT/연산자끼워넣기.txt', 'r')

def get_max_min(idx, res):
    global max_value, min_value
    if idx == N:
        max_value = max(max_value, res)
        min_value = min(min_value, res)
        return
    for i in range(4):
        if sign_cnt[i] == 0: continue
        if i == 0:
            sign_cnt[i] -= 1
            get_max_min(idx+1, res+numbers[idx])
            sign_cnt[i] += 1
        elif i == 1:
            sign_cnt[i] -= 1
            get_max_min(idx+1, res-numbers[idx])
            sign_cnt[i] += 1
        elif i == 2:
            sign_cnt[i] -= 1
            get_max_min(idx+1, res*numbers[idx])
            sign_cnt[i] += 1
        elif i == 3:
            sign_cnt[i] -= 1
            get_max_min(idx+1, res//numbers[idx] if res >= 0 else -(abs(res)//numbers[idx]))
            sign_cnt[i] += 1

N = int(input())
numbers = [*map(int, input().split())]
sign_cnt = [*map(int, input().split())]
max_value = -int(1e9)
min_value = int(1e9)
get_max_min(1, numbers[0])
print(max_value)
print(min_value)
