import sys
sys.stdin = open("../INPUT/1260.txt", "r")

from collections import deque

def dfs(node):
    visited_dfs[node] = 1
    answer_dfs.append(node)
    for next in sorted(G[node]):
        if visited_dfs[next]: continue
        dfs(next)

def bfs(node):
    visited_bfs = [0] * (N+1)
    visited_bfs[node] = 1
    answer_bfs.append(node)
    Q = deque()
    Q.append(node)
    while Q:
        now = Q.popleft()
        for next in sorted(G[now]):
            if visited_bfs[next]: continue
            visited_bfs[next] = 1
            Q.append(next)
            answer_bfs.append(next)

N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
visited_dfs = [0] * (N+1)
answer_dfs = []
answer_bfs = []
dfs(V)
bfs(V)
print(*answer_dfs)
print(*answer_bfs)