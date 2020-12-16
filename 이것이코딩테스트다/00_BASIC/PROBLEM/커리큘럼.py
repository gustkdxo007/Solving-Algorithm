import sys
sys.stdin = open('../INPUT/커리큘럼.txt', 'r')

from collections import deque
import copy

N = int(input())
indegree = [0] * (N+1)
time = [0] * (N+1)
G = [[] for _ in range(N+1)]
for n in range(1, N+1):
    data = [*map(int, input().split())]
    time[n] = data[0]
    for d in data[1:-1]:
        indegree[n] += 1
        G[d].append(n)

def topology_sort():
    result = copy.copy(time)
    Q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)
    while Q:
        now = Q.popleft()
        for g in G[now]:
            result[g] = max(result[g], result[now]+time[g])
            indegree[g] -= 1
            if indegree[g] == 0:
                Q.append(g)
    for r in range(1, N+1):
        print(result[r])

topology_sort()