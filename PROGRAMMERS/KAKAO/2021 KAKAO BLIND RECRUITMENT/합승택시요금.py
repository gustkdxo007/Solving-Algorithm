import heapq

def dijkstra(s, matrix):
    INF = int(1e9)
    D = [INF] * len(matrix)
    D[s] = 0
    Q = []
    heapq.heappush(Q, (0, s))
    while Q:
        cost, to = heapq.heappop(Q)
        for v, c in matrix[to]:
            tmp = cost + c
            if D[v] > tmp:
                D[v] = tmp
                heapq.heappush(Q, (tmp, v))
    return D

def solution(n, s, a, b, fares):
    matrix = [[] for _ in range(n)]
    for f, t, c in fares:
        matrix[f-1].append((t-1, c))
        matrix[t-1].append((f-1, c))
    D1 = dijkstra(s-1, matrix)
    total = D1[a-1] + D1[b-1]
    for i in range(n):
        if D1[i] == 0 or D1[i] == int(1e9): continue
        if D1[i] < total:
            D2 = dijkstra(i, matrix)
            total = min(total, D1[i] + D2[a-1] + D2[b-1])
    return total

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))