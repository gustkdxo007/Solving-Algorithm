import sys
sys.stdin = open('../INPUT/1753.txt', 'r')

import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    D[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if D[now] < dist: continue
        for n, wei in graph[now]:
            cost = dist + wei
            if D[n] > cost:
                D[n] = cost
                heapq.heappush(heap, (cost, n))

V, E = map(int, input().split())
INF = int(1e9)
start = int(input())
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
D = [INF] * (V+1)

dijkstra(start)
for i in D[1:]:
    print(i if i != INF else 'INF')