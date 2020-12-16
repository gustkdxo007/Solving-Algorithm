import sys
sys.stdin = open('../INPUT/음료수얼려먹기.txt', 'r')

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(r, c):
    visited[r][c] = 1
    for d in range(4):
        dr, dc = r+dx[d], c+dy[d]
        if dr < 0 or dr >= N or dc < 0 or dc >= M: continue
        if not visited[dr][dc] and not matrix[dr][dc]:
            dfs(dr, dc)

for t in range(T):
    N, M = map(int, input().split())
    matrix = [[*map(int, input())] for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if not matrix[i][j] and not visited[i][j]:
                result += 1
                dfs(i, j)
    print(result)