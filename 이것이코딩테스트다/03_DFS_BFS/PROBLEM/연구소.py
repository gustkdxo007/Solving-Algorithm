import sys
sys.stdin = open('../INPUT/연구소.txt', 'r')

N, M = map(int, input().split())
lab = [[*map(int, input().split())] for _ in range(N)]
tmp = [[0]*M for _ in range(N)]

result = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def virus(x, y):
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or tmp[nx][ny] == 1 or tmp[nx][ny] == 2: continue
        tmp[nx][ny] = 2
        virus(nx, ny)

def get_safe():
    global result
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    result = max(result, cnt)
    return

def dfs(cnt):
    if cnt == 3:
        for i in range(N):
            for j in range(M):
                tmp[i][j] = lab[i][j]
        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 2:
                    virus(i, j)
        get_safe()
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                dfs(cnt+1)
                lab[i][j] = 0


dfs(0)
print(result)