import sys
sys.stdin = open('../INPUT/인구이동.txt', 'r')

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    global check
    visited[x][y] = 1
    Q = deque()
    Q.append((x, y))
    share = [(x,y)]
    people = board[x][y]
    cnt = 1
    while Q:
        i, j = Q.popleft()
        for d in range(4):
            ni, nj = i+dx[d], j+dy[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if L <= abs(board[i][j] - board[ni][nj]) <= R:
                visited[ni][nj] = 1
                people += board[ni][nj]
                cnt += 1
                share.append((ni, nj))
                Q.append((ni, nj))
    balance = people // cnt
    if len(share) > 1:
        check = True
    for xx, yy in share:
        board[xx][yy] = balance

N, L, R = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
result = 0
while True:
    visited = [[0]*N for _ in range(N)]
    check = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
    if not check: break
    result += 1
print(result)