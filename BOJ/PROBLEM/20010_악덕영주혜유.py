import sys
sys.stdin = open('../INPUT/20010.txt', 'r')

import heapq

N, K = map(int, input().split())
G = [[] for _ in range(N)]
visited = [0] * N
for _ in range(K):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

Q = []
heapq.heappush(Q, (0, 0, 0))
total_weight = 0

mst = [[] for _ in range(N)]

while Q:
    w, v, n = heapq.heappop(Q)
    if not visited[v]:
        visited[v] = 1
        mst[n].append((v, w))
        mst[v].append((n, w))
        total_weight += w
        for next, cost in G[v]:
            if visited[next]: continue
            heapq.heappush(Q, (cost, next, v))
print(total_weight)
mst[0] = mst[0][2:]

def dfs(now, prev):
    res = 0
    for v, c in mst[now]:
        if v == prev: continue
        res = max(res, dfs(v, now)+c)
    return res

answer = 0

for i in range(N):
    if len(mst[i]) == 1:
        answer = max(answer, dfs(i, -1))

print(answer)