import sys
sys.stdin = open("../INPUT/2458.txt", "r")

# N, M = map(int, input().split())
# board = [[0]*(N+1) for _ in range(N+1)]
# answer = 0
# for _ in range(M):
#     a, b = map(int, input().split())
#     board[a][b] = 1
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if board[i][k] == 1 and board[k][j] == 1:
#                 board[i][j] = 1
#
# for i in range(1, N+1):
#     tmp = 0
#     for j in range(1, N+1):
#         if i == j: continue
#         if board[i][j]:
#             tmp += board[i][j]
#         else:
#             tmp += board[j][i]
#     if tmp == (N-1):
#         answer += 1
# print(answer)
from collections import defaultdict, deque

N, M = map(int, input().split())

order_h = defaultdict(list)
order_l = defaultdict(list)
degree = [0] * (N+1)
for _ in range(M):
    Low, High = map(int, input().split())
    order_h[Low].append(High)
    order_l[High].append(Low)


for key in order_h.keys():
    visited = [0] * (N+1)
    Q = deque()
    Q.append(key)
    visited[key] = 1

    while Q:
        now = Q.popleft()
        if now not in order_h.keys():
            continue
        for element in order_h[now]:
            if visited[element] == 0:
                visited[element] = 1
                degree[element] += 1
                Q.append(element)

for key in order_l.keys():
    visited = [0] * (N+1)
    Q = deque()
    Q.append(key)
    visited[key] = 1

    while Q:
        now = Q.popleft()
        if now not in order_l.keys():
            continue
        for element in order_l[now]:
            if visited[element] == 0:
                visited[element] = 1
                degree[element] += 1
                Q.append(element)
print(degree.count(N-1))