import sys
sys.stdin = open('../INPUT/16929.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(a, b, sa, sb, dot, cnt):
    global result
    for d in range(4):
        tx, ty = a+dx[d], b+dy[d]
        if tx < 0 or tx >= N or ty < 0 or ty >= M: continue
        if visited[tx][ty] and tx == sa and ty == sb and cnt >= 4:
            result = 'Yes'
            return
        if not visited[tx][ty] and game[tx][ty] == dot:
            visited[tx][ty] = 1
            dfs(tx, ty, sa, sb, dot, cnt+1)


N, M = map(int, input().split())
game = [input() for _ in range(N)]
result = 'No'
dots_cnt = dict()
candidate_dots = []
for l in game:
    for c in l:
        if c in dots_cnt:
            dots_cnt[c] += 1
        else:
            dots_cnt[c] = 1
for key, val in dots_cnt.items():
    if val >= 4:
        candidate_dots.append(key)

visited = [[0] * M for _ in range(N)]

for i in range(N):
    breaker = False
    for j in range(M):
        if game[i][j] in candidate_dots:
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            dfs(i, j, i, j, game[i][j], 1)
            if result == 'Yes':
                breaker = True
                break
    if breaker:
        break
print(result)