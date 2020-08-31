import sys
sys.stdin = open('../INPUT/1486.txt', 'r')

# 부분집합 중에 특정 조건을 만족하는 부분집합을 찾는 문제

# 멱집합 구하기
def power_set(selected, idx):
    global min_height
    if idx == N:
        sum_h = 0
        for i in range(N):
            if selected[i]:
                sum_h += heights[i]
        if sum_h >= B and (sum_h - B) < min_height:
            # B 이상 중 최소인지 확인
            min_height = sum_h - B

        return
    selected[idx] = 1
    power_set(selected, idx+1)
    selected[idx] = 0
    power_set(selected, idx+1)

# 총 합으로 구하기
def power_set2(idx, sum_h):
    global min_height
    if idx == N:
        if sum_h >= B and min_height > (sum_h - B):
            min_height = sum_h - B
        return
    if sum_h >= B + min_height:
        return
    power_set2(idx + 1, sum_h + heights[idx])
    power_set2(idx + 1, sum_h)

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    heights = [*map(int, input().split())]
    min_height = 200000
    # power_set([0]*N, 0)
    power_set2(0, 0)
    print('#{} {}'.format(t, min_height))