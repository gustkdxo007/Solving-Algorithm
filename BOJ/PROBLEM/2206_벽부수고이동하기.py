import sys
sys.stdin = open("../INPUT/2206.txt", "r")

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move(a, b):
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[a][b][0] = 1
    Q = deque()
    Q.append((a, b, 0))
    while Q:
        x, y, z = Q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y]
        for d in range(4):
            tx, ty = x+dx[d], y+dy[d]
            if tx < 0 or tx >= N or ty < 0 or ty >= M: continue
            if maps[tx][ty] == 0 and visited[tx][ty][z] == 0:
                visited[tx][ty][z] = visited[x][y][z] + 1
                Q.append((tx, ty, z))
            if z == 0 and maps[tx][ty] == 1 and visited[tx][ty][z] == 0:
                visited[tx][ty][z+1] = visited[x][y][z] + 1
                Q.append((tx, ty, z+1))
    return [-1]

N, M = map(int, input().split())
maps = [[*map(int, list(input()))] for _ in range(N)]
print(max(move(0, 0)))