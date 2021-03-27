import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(land, height):
    answer = 0
    N = len(land)
    cnt = N * N
    visited = [[0] * N for _ in range(N)]
    Q = []
    heapq.heappush(Q, (0, 0, 0))
    while Q:
        h, x, y = heapq.heappop(Q)
        if visited[x][y]: continue
        visited[x][y] = 1
        answer += h
        cnt -= 1
        if cnt == 0: break
        for d in range(4):
            tx, ty = x+dx[d], y+dy[d]
            if tx < 0 or tx >= N or ty < 0 or ty >= N or visited[tx][ty]: continue
            gap = abs(land[x][y] - land[tx][ty])
            gap = gap if gap > height else 0
            heapq.heappush(Q, (gap, tx, ty))
    return answer


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))