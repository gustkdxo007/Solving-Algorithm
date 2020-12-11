import sys
sys.stdin = open('위상정렬.txt', 'r')

from collections import deque

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
indegree = [0] * (V+1)
for e in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    indegree[b] += 1

def get_route():
    result = []
    Q = deque()

    for i in range(1, V+1):
        if not indegree[i]:
            Q.append(i)

    while Q:
        now = Q.popleft()
        result.append(now)
        for i in G[now]:
            indegree[i] -= 1
            if not indegree[i]:
                Q.append(i)
    print(*result)
get_route()