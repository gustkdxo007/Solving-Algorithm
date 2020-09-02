import sys
sys.stdin = open('../INPUT/1226.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 반복문
def dfs(r, c):
    visited = [[0] * 16 for _ in range(16)]
    stack = list()
    stack.append((r, c))

    while stack:  # 스택이 비어있지 않다면 계속 반복
        cr, cc = stack.pop()
        visited[cr][cc] = 1
        for d in range(4):
            tr, tc = cr + dr[d], cc + dc[d]
            # 범위 내에 있고, 방문하지 않았고, 통로여야 함
            if 0 <= tr < 16 and 0 <= tc < 16 and not visited[tr][tc] and not maze[tr][tc]:
                stack.append((tr, tc))
            elif maze[tr][tc] == 3:
                return 1
    return 0

# 재귀
def dfs1(r, c):
    visited[r][c] = 1
    for d in range(4):
        tr, tc = r + dr[d], c + dc[d]
        if maze[tr][tc] == 3:
            return 1
        if 0 <= tr < 16 and 0 <= tc < 16 and not visited[tr][tc] and not maze[tr][tc]:
            if dfs1(tr, tc):
                return 1
    return 0

T = 10
for t in range(T):
    tc = input()
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    result = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                result = dfs1(i, j)
                break
    print('#{} {}'.format(tc, result))