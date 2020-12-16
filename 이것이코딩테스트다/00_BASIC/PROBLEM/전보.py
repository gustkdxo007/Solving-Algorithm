import sys
sys.stdin = open('../INPUT/전보.txt', 'r')
import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
G = [[] for _ in range(N+1)]
D = [INF] * (N+1)

for i in range(M):
    f, t, c = map(int, input().split())
    G[f].append((t, c))

def get_result(start):
    Q = []
    D[start] = 0
    heapq.heappush(Q, (0, start))
    while Q:
        dist, now = heapq.heappop(Q)
        if D[now] < dist: continue
        for v, c in G[now]:
            cost = dist + c
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(Q, (cost, v))
get_result(C)
cnt = 0
max_ = 0
for i in range(1, N+1):
    if D[i] != INF:
        cnt += 1
        max_ = max(max_, D[i])
print(cnt-1, max_)