import sys
sys.stdin = open('../INPUT/뱀.txt', 'r')
# from collections import deque
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def turn_head(d, c):
#     return (d+1) % 4 if c == 'D' else (d-1) % 4
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     board = [[0]*(N+1) for _ in range(N+1)]
#     snake = deque()
#     seconds = 0
#     turn = []
#     D = 1
#     hx, hy = 1, 1
#     for _ in range(int(input())):
#         r, c = map(int, input().split())
#         board[r][c] = 'a'
#     for _ in range(int(input())):
#         t, d = input().split()
#         turn.append((int(t), d))
#     length = len(turn)
#     snake.append((1, 1))
#     board[1][1] = 's'
#     idx = 0
#     while True:
#         nx, ny = hx+dx[D], hy+dy[D]
#         seconds += 1
#         if nx < 1 or nx > N or ny < 1 or ny > N or board[nx][ny] == 's':
#             break
#         if not board[nx][ny]:
#             ox, oy = snake.popleft()
#             board[ox][oy] = 0
#         hx, hy = nx, ny
#         board[nx][ny] = 's'
#         snake.append((nx, ny))
#         if idx < length and turn[idx][0] == seconds:
#             D = turn_head(D, turn[idx][1])
#             idx += 1
#     print(seconds)

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_head(d, c):
    return (d+1) % 4 if c == 'D' else (d-1) % 4


N = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
snake = deque()
seconds = 0
turn = []
D = 1
hx, hy = 1, 1
for _ in range(int(input())):
    r, c = map(int, input().split())
    board[r][c] = 'a'
for _ in range(int(input())):
    t, d = input().split()
    turn.append((int(t), d))
length = len(turn)
snake.append((1, 1))
board[1][1] = 's'
idx = 0
while True:
    nx, ny = hx+dx[D], hy+dy[D]
    seconds += 1
    if nx < 1 or nx > N or ny < 1 or ny > N or board[nx][ny] == 's':
        break
    if not board[nx][ny]:
        ox, oy = snake.popleft()
        board[ox][oy] = 0
    hx, hy = nx, ny
    board[nx][ny] = 's'
    snake.append((nx, ny))
    if idx < length and turn[idx][0] == seconds:
        D = turn_head(D, turn[idx][1])
        idx += 1
print(seconds)