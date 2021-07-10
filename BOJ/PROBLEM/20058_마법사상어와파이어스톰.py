import sys
sys.stdin = open('../INPUT/20058.txt', 'r')

import copy
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, Q = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))
visited = [[0] * (2**N) for _ in range(2**N)]

def rotate_90(arr, s):
    new_arr = [[0] * s for _ in range(s)]
    for i in range(s):
        for j in range(s):
            new_arr[j][s-i-1] = arr[i][j]
    return new_arr

def melt_ice():
    melting = []
    for i in range(2**N):
        for j in range(2**N):
            if not boards[i][j]: continue
            cnt = 0
            for d in range(4):
                tx, ty = i+dx[d], j+dy[d]
                if tx < 0 or tx >= 2**N or ty < 0 or ty >= 2**N or not boards[tx][ty]: continue
                cnt += 1
            if cnt < 3:
                melting.append((i, j))
    for x, y in melting:
        boards[x][y] -= 1

def bfs(r, c):
    Q = deque()
    visited[r][c] = 1
    Q.append((r, c))
    cnt = 0
    while Q:
        x, y = Q.popleft()
        cnt += 1
        for d in range(4):
            tx, ty = x+dx[d], y+dy[d]
            if tx < 0 or tx >= 2 ** N or ty < 0 or ty >= 2 ** N or visited[tx][ty] or not boards[tx][ty]: continue
            visited[tx][ty] = 1
            Q.append((tx, ty))
    return cnt

for l in L:
    size = 2 ** l
    n = (2 ** N) // (2 ** l)
    for i in range(0, 2 ** N, size):
        for j in range(0, 2 ** N, size):
            arr = []
            for r in range(i, i+size):
                arr.append(boards[r][j:j+size])
            arr = copy.deepcopy(rotate_90(arr, size))
            for ii in range(size):
                for jj in range(size):
                    boards[ii+i][jj+j] = arr[ii][jj]
    melt_ice()
total = 0
for row in boards:
    total += sum(row)
print(total)

max_set = 0
for i in range(2**N):
    for j in range(2**N):
        if not boards[i][j] or visited[i][j]: continue
        max_set = max(max_set, bfs(i, j))
print(max_set)

