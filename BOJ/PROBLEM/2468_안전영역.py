import sys
sys.stdin = open("../INPUT/2468.txt", "r")

sys.setrecursionlimit(10000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visited[x][y] = 1
    for d in range(4):
        tx, ty = x+dx[d], y+dy[d]
        if tx < 0 or tx >= N or ty < 0 or ty >= N or visited[tx][ty] or heights[tx][ty] == 0: continue
        dfs(tx, ty)

N = int(input())
heights = [[*map(int, input().split())] for _ in range(N)]
answer = 1
h = 1
while True:
    for i in range(N):
        for j in range(N):
            if heights[i][j] and heights[i][j] <= h:
                heights[i][j] = 0
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or heights[i][j] == 0: continue
            cnt += 1
            dfs(i, j)
    if cnt == 0: break
    answer = max(answer, cnt)
    h += 1
print(answer)