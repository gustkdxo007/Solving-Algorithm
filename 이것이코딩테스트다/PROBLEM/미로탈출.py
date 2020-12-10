import sys
sys.stdin = open('../INPUT/미로탈출.txt', 'r')
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
miro = [[*map(int, input())] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
Q = deque()
Q.append((0, 0))
visited[0][0] = 1
while Q:
    r, c = Q.popleft()
    if r == N-1 and c == M-1:
        print(visited[r][c])
        break
    for d in range(4):
        dr, dc = r+dx[d], c+dy[d]
        if dr < 0 or dr >= N or dc < 0 or dc >= M: continue
        if miro[dr][dc] and not visited[dr][dc]:
            visited[dr][dc] = visited[r][c] + 1
            Q.append((dr, dc))