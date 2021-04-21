import sys
sys.stdin = open("../INPUT/10451.txt", "r")

sys.setrecursionlimit(10000)

T = int(input())
for t in range(T):
    N = int(input())
    P = [0] + [*map(int, input().split())]
    visited = [0] * (N + 1)
    answer = 0

    def dfs(n):
        visited[n] += 1
        if visited[n] > 1: return True
        return dfs(P[n])

    for i in range(1, N+1):
        if visited[i]: continue
        if dfs(i):
            answer += 1
    print(answer)