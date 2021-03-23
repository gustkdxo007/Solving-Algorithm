import sys
sys.stdin = open('../INPUT/1916.txt')

import heapq

def dijkstra(s):
    Q = []
    D[s] = 0
    heapq.heappush(Q, (0, s))

    while Q:
        dist, now = heapq.heappop(Q)
        if D[now] < dist: continue
        for t, c in G[now]:
            cost = dist + c
            if cost < D[t]:
                D[t] = cost
                heapq.heappush(Q, (cost, t))

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    G[s].append((e, c))

D = [int(1e9)] * (N+1)

start, end = map(int, input().split())
dijkstra(start)
print(D[end])
