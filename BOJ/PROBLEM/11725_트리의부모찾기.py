import sys
sys.stdin = open("../INPUT/11725.txt", "r")

from collections import deque

N = int(input())
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)
parents = [0] * (N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

Q = deque()
Q.append(1)
visited[1] = 1
while Q:
    now = Q.popleft()
    for next in G[now]:
        if visited[next]: continue
        visited[next] = 1
        parents[next] = now
        Q.append(next)
for i in range(2, N+1):
    print(parents[i])
