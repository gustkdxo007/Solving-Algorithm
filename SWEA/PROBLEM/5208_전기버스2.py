import sys
sys.stdin = open("../INPUT/5208.txt", "r")

# idx: 정류장 번호
# cnt: 배터리 교환 횟수
# remain: 현재 배터리 잔량
def dfs(idx, cnt, remain):
    global result
    # 마지막 정류장까지 고려했으면, 더 이상 진행하지 않음
    if cnt >= result:
        return
    if idx == N:
        result = min(result, cnt)
        return
    # 선택할 수 있는 경우의 수
    # 배터리를 갈거나
    dfs(idx+1, cnt+1, stops[idx])
    # 갈지 않거나 => 배터리가 남아있어야 할 수 있는 결정
    if remain - 1 > 0:
        dfs(idx+1, cnt, remain-1)


T = int(input())
for t in range(1, T+1):
    stops = [*map(int, input().split())]
    N = stops[0]
    result = 10000
    dfs(2, 0, stops[1])
    print("#{} {}".format(t, result))