import sys
sys.stdin = open('../INPUT/특정거리의도시찾기.txt', 'r')

from collections import deque

N, M, K, X = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    f, t = map(int, input().split())
    G[f].append(t)
visited = [-1] * (N+1)
visited[X] = 0
Q = deque([X])
while Q:
    now = Q.popleft()
    for city in G[now]:
        if visited[city] == -1:
            visited[city] = visited[now] + 1
            Q.append(city)
check = False
for i in range(1, N+1):
    if visited[i] == K:
        check = True
        print(i)
if not check:
    print(-1)