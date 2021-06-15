import sys
sys.stdin = open("../INPUT/17836.txt", "r")

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(board, n, m, t):
    visited = [[0] * m for _ in range(n)]
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = 1
    gram = int(1e9)
    while Q:
        x, y = Q.popleft()
        if board[x][y] == 2:
            gram = abs(n-1-x) + abs(m-1-y) + visited[x][y] - 1
        if x == n-1 and y == m-1:
            return min(gram, visited[x][y] - 1)
        for d in range(4):
            tx, ty = x+dx[d], y+dy[d]
            if tx < 0 or tx >= n or ty < 0 or ty >= m or visited[tx][ty] or board[tx][ty] == 1: continue
            visited[tx][ty] = visited[x][y] + 1
            Q.append((tx, ty))
    return gram



N, M, T = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
answer = bfs(maps, N, M, T)
print(answer if answer <= T else 'Fail')

