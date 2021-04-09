import sys
sys.stdin = open("../INPUT/3109.txt")

dx = [-1, 0, 1]

def dfs(x, y):
    global answer
    if y == C-1:
        answer += 1
        return True
    for d in range(3):
        tx, ty = x+dx[d], y+1
        if tx < 0 or tx >= R or ty < 0 or ty >= C or visited[tx][ty] or maps[tx][ty] == 'x': continue
        visited[tx][ty] = 1
        if dfs(tx, ty):
            return True
    return False

R, C = map(int, input().split())
maps = [input() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
answer = 0
for i in range(R):
    visited[i][0] = 1
    dfs(i, 0)
print(answer)
