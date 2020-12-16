import sys
sys.stdin = open('../INPUT/게임개발.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [[*map(int, input().split())] for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

result = 1
turn_cnt = 0
while True:
    turn_left()
    dr, dc = r+dx[d], c+dy[d]
    if maps[dr][dc] == 0 and visited[dr][dc] == 0:
        maps[dr][dc] = 1
        result += 1
        turn_cnt = 0
        r, c = dr, dc
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        dr, dc = r-dx[d], r-dy[d]
        if maps[dr][dc] == 1:
            break
        r, c = dr, dc
        turn_cnt = 0

print(result)

