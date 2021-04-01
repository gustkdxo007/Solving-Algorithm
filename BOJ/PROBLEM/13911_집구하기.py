import sys
sys.stdin = open("../INPUT/13911.txt")

import heapq

def dijkstra(start):
    global answer
    Q = []
    D = [int(1e9)] * (V+3)
    heapq.heappush(Q, (0, start))
    D[start] = 0
    while Q:
        dist, now = heapq.heappop(Q)
        if D[now] < dist: continue
        for v, c in G[now]:
            # if v == V+1 or v == V+2: continue
            cost = dist + c
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(Q, (cost, v))
    return D

V, E = map(int, input().split())
G = [[] for _ in range(V+3)]
answer = int(1e9)
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

star_n, star_x = map(int, input().split())
stars = [*map(int, input().split())]
mac_n, mac_x = map(int, input().split())
macs = [*map(int, input().split())]
for s in stars:
    G[V+1].append((s, 0))
    # G[s].append((V+1, 0))
for m in macs:
    G[V+2].append((m, 0))
    # G[m].append((V+2, 0))

star_dist = dijkstra(V+1)
mac_dist = dijkstra(V+2)

for i in range(1, V+1):
    if i in stars or i in macs: continue
    if star_dist[i] > star_x or mac_dist[i] > mac_x: continue
    answer = min(answer, star_dist[i] + mac_dist[i])

print(answer if answer != int(1e9) else -1)
