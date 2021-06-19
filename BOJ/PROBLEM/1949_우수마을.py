import sys
sys.stdin = open("../INPUT/1949.txt", "r")
sys.setrecursionlimit(20000)

N = int(input())
P = [0] + [*map(int, input().split())]
G = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visited = [0] * (N+1)
DP = [[0] * 2 for _ in range(N+1)]


def dfs(start):
    visited[start] = 1
    DP[start][0] = P[start]
    for next in G[start]:
        if visited[next]: continue
        dfs(next)
        DP[start][0] += DP[next][1]
        DP[start][1] += max(DP[next][0], DP[next][1])

dfs(1)
print(max(DP[1][0], DP[1][1]))