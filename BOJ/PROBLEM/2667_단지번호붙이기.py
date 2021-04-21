import sys
sys.stdin = open("../INPUT/2667.txt", "r")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    for d in range(4):
        tx, ty = x+dx[d], y+dy[d]
        if tx < 0 or tx >= N or ty < 0 or ty >= N or visited[tx][ty] or not maps[tx][ty]: continue
        dfs(tx, ty)

N = int(input())
maps = [[*map(int, list(input()))] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if not maps[i][j] or visited[i][j]: continue
        dfs(i, j)
        answer.append(cnt)
print(len(answer))
answer.sort()
for x in answer:
    print(x)