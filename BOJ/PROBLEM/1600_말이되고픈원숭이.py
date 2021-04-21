import sys
sys.stdin = open("../INPUT/1600.txt", "r")

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
hdx = [-2, -1, 1, 2, 2, 1, -1, -2]
hdy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]
    Q = deque()
    Q.append((0, 0, 0))
    visited[0][0][0] = 1
    while Q:
        x, y, k = Q.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][k] - 1
        for d in range(4):
            tx, ty = x+dx[d], y+dy[d]
            if tx < 0 or tx >= H or ty < 0 or ty >= W or visited[tx][ty][k] or board[tx][ty]: continue
            visited[tx][ty][k] = visited[x][y][k] + 1
            Q.append((tx, ty, k))
        for d in range(8):
            tx, ty = x+hdx[d], y+hdy[d]
            if tx < 0 or tx >= H or ty < 0 or ty >= W or k+1 > K or visited[tx][ty][k+1] or board[tx][ty]: continue
            visited[tx][ty][k+1] = visited[x][y][k] + 1
            Q.append((tx, ty, k+1))
    return -1

K = int(input())
W, H = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(H)]
print(bfs())