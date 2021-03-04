import heapq

def dijkstra(s, N, G):
    D = [int(1e9) for _ in range(N+1)]
    D[s] = 0
    Q = []
    heapq.heappush(Q, (0, s))
    while Q:
        time, now = heapq.heappop(Q)
        if D[now] < time: continue
        for f, c in G[now]:
            cost = time + c
            if cost < D[f]:
                D[f] = cost
                heapq.heappush(Q, (cost, f))
    return D


def solution(N, road, K):
    answer = 0
    G = [[] for _ in range(N+1)]
    for f, t, c in road:
        G[f].append((t, c))
        G[t].append((f, c))
    D = dijkstra(1, N, G)
    for i in range(1, N+1):
        if D[i] <= K:
            answer += 1
    return answer


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))