import sys
sys.stdin = open("../INPUT/7576.txt", "r")

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check_growed():
    answer = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
            answer = max(answer, visited[i][j])
    return answer - 1

M, N = map(int, input().split())
box = [[*map(int, input().split())] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
total = N * M
Q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            visited[i][j] = 1
            Q.append((i, j))

while Q:
    x, y = Q.popleft()
    for d in range(4):
        tx, ty = x+dx[d], y+dy[d]
        if tx < 0 or tx >= N or ty < 0 or ty >= M or visited[tx][ty] or box[tx][ty] != 0: continue
        Q.append((tx, ty))
        box[tx][ty] = 1
        visited[tx][ty] = visited[x][y] + 1

print(check_growed())