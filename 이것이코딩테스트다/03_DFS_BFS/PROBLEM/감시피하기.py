import sys
sys.stdin = open('../INPUT/감시피하기.txt', 'r')

def is_ok(x, y):
    for d in range(4):
        nx, ny = x, y
        while True:
            nx, ny = nx+dx[d], ny+dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or tmp[nx][ny] == 'O': break
            if tmp[nx][ny] == 'S':
                return False
    return True

def set_o(cnt):
    global result
    if cnt == 3:
        for i in range(N):
            for j in range(N):
                tmp[i][j] = board[i][j]
        for i in range(N):
            for j in range(N):
                if tmp[i][j] == 'T':
                    if not is_ok(i, j):
                        return
        result = 'YES'
        return
        pass
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                set_o(cnt+1)
                board[i][j] = 'X'

N = int(input())
board = [input().split() for _ in range(N)]
tmp = [[0]*N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = 'NO'
set_o(0)
print(result)