import sys
sys.stdin = open('다익스트라.txt', 'r')

# 우선순위 큐를 이용한 다익스트라
import heapq
N, M = map(int, input().split())
start = int(input())
G = [[] for _ in range(N+1)]
INF = int(1e9)
D = [INF] * (N+1)
for i in range(M):
    f, t, c = map(int, input().split())
    G[f].append((t, c))

def get_result(s):
    Q = []
    heapq.heappush(Q, (0, s))
    D[s] = 0
    while Q:
        dist, now = heapq.heappop(Q)
        if D[now] < dist: continue
        for v, c in G[now]:
            cost = dist + c
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(Q, (cost, v))
get_result(start)
print(D)

# 기본 다익스트라
# N, M = map(int, input().split())
# start = int(input())
# G = [[] for _ in range(N+1)]
# visited = [0] * (N+1)
# INF = int(1e9)
# D = [INF] * (N+1)
#
# for i in range(M):
#     f, t, c = map(int, input().split())
#     G[f].append((t, c))
#
# def get_smallest_node():
#     min_ = INF
#     index = 0
#     for i in range(1, N+1):
#         if not visited[i] and D[i] < min_:
#             min_ = D[i]
#             index = i
#     return index
#
# def get_result(s):
#     D[s] = 0
#     visited[s] = 1
#     for v, c in G[s]:
#         D[v] = c
#
#     for i in range(N-1):
#         V = get_smallest_node()
#         visited[V] = 1
#         for v, c in G[V]:
#             cost = D[V] + c
#             if cost < D[v]:
#                 D[v] = cost
#
# get_result(start)
# print(D)
