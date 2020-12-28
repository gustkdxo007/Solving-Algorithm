import sys
sys.stdin = open('../INPUT/경쟁적전염.txt', 'r')

import heapq

N, K = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
S, X, Y = map(int, input().split())
visited = [[0]*N for _ in range(N)]
Q = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(N):
    for j in range(N):
        if board[i][j]:
            heapq.heappush(Q, (board[i][j], i, j))
second = 0
while second < S:
    second += 1
    new_Q = []
    while Q:
        n, x, y = heapq.heappop(Q)
        visited[x][y] = 1
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] or board[nx][ny]: continue
            board[nx][ny] = n
            heapq.heappush(new_Q, (n, nx, ny))
    Q = new_Q
print(board[X-1][Y-1])