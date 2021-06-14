import sys
sys.stdin = open("../INPUT/7562.txt", "r")

from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(board, x, y, gx, gy, n):
    visited = [[-1] * n for _ in range(n)]
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 0
    while Q:
        ox, oy = Q.popleft()
        if ox == gx and oy == gy:
            return visited[ox][oy]
        for d in range(8):
            tx, ty = ox+dx[d], oy+dy[d]
            if tx < 0 or tx >= n or ty < 0 or ty >= n or visited[tx][ty] >= 0: continue
            visited[tx][ty] = visited[ox][oy] + 1
            Q.append((tx, ty))
    return 0

    pass

T = int(input())
for t in range(T):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    k_x, k_y = map(int, input().split())
    m_x, m_y = map(int, input().split())
    print(bfs(board, k_x, k_y, m_x, m_y, N))