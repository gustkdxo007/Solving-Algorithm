from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = 1
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            tx, ty = x+dx[d], y+dy[d]
            if tx < 0 or tx >= N or ty < 0 or ty >= M or not maps[tx][ty] or visited[tx][ty]: continue
            visited[tx][ty] = visited[x][y] + 1
            Q.append((tx, ty))
    return visited[N-1][M-1] if visited[N-1][M-1] else -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))