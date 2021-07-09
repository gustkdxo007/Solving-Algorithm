import sys
sys.stdin = open('../INPUT/5212.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
changed = []
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'X':
            r, c = i, j
            cnt = 0
            for d in range(4):
                tr = r+dr[d]
                tc = c+dc[d]
                if tr < 0 or tr >= R or tc < 0 or tc >= C or maps[tr][tc] == '.':
                    cnt += 1
            if cnt >= 3:
                changed.append((i, j))
for x, y in changed:
    maps[x][y] = '.'

x1, x2 = R, -1
y1, y2 = C, -1
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'X':
            x1 = min(x1, i)
            x2 = max(x2, i)
            y1 = min(y1, j)
            y2 = max(y2, j)
for i in range(x1, x2+1):
    print(''.join(maps[i][y1:y2+1]))
