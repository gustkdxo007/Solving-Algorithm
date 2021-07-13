import sys
sys.stdin = open('../INPUT/14567.txt', 'r')

from collections import deque

N, M = map(int, input().split())
pre_sub = [0] * (N+1)
visited = [0] * (N+1)
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    pre_sub[b] += 1

Q = deque()

for i in range(1, N+1):
    if not pre_sub[i]:
        Q.append(i)
        visited[i] += 1

while Q:
    now = Q.popleft()
    for next in G[now]:
        pre_sub[next] -= 1
        visited[next] = visited[now] + 1
        if not pre_sub[next]:
            Q.append(next)

print(*visited[1:])