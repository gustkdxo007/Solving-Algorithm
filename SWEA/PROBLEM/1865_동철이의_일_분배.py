import sys
sys.stdin = open('../INPUT/1865.txt', 'r')

def solve(idx, rate):  # idx : 행의 번호
    global result
    # 재귀를 더 이상 하지 않는 조건
    if result >= rate: return
    if idx == N:
        result = max(result, rate)
        return
    # 현재 상태에서 내가 할 수 있는 모든 조건 고려해보기
    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        solve(idx+1, rate * rates[idx][i])
        visited[i] = 0




T = int(input())
for t in range(1, T+1):
    N = int(input())
    rates = [[*map(lambda x: int(x) / 100, input().split())] for _ in range(N)]
    visited = [0] * N
    result = 0
    solve(0, 1)
    # print("#{}".format(t), format(result*100, ".6f"))
    print("#%d %0.6f" %(t, round(result*100, 6)))