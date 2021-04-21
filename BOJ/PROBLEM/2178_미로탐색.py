import sys
sys.stdin = open("../INPUT/2178.txt", "r")

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
miro = [[*map(int, list(input()))] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
Q = deque()
Q.append((0, 0))
visited[0][0] = 1
while Q:
    x, y = Q.popleft()
    for d in range(4):
        tx, ty = x+dx[d], y+dy[d]
        if tx < 0 or tx >= N or ty < 0 or ty >= M or visited[tx][ty] or not miro[tx][ty]: continue
        visited[tx][ty] = visited[x][y] + 1
        Q.append((tx, ty))
print(visited[N-1][M-1])