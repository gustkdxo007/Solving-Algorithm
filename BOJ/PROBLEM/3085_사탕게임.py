import sys
sys.stdin = open('../INPUT/3085.txt')

def get_cnt(arr):
    candy = arr[0]
    cnt = 1
    max_cnt = 0
    for i in range(1, len(arr)):
        if candy != arr[i]:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
            candy = arr[i]
        else:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    return max_cnt

N = int(input())
board = [list(input()) for _ in range(N)]
result = 0
for i in range(N):
    result = max(result, get_cnt(board[i]))
    for j in range(1, N):
        board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
        result = max(result, get_cnt(board[i]))
        sero1 = [0] * N
        sero2 = [0] * N
        for k in range(N):
            sero1[k] = board[k][j-1]
            sero2[k] = board[k][j]
        result = max(result, get_cnt(sero1))
        result = max(result, get_cnt(sero2))
        board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]

new_board = []
for i in range(N):
    sero = [0] * N
    for j in range(N):
        sero[j] = board[j][i]
    new_board.append(sero)

for i in range(N):
    result = max(result, get_cnt(new_board[i]))
    for j in range(1, N):
        new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
        result = max(result, get_cnt(new_board[i]))
        sero1 = [0] * N
        sero2 = [0] * N
        for k in range(N):
            sero1[k] = new_board[k][j - 1]
            sero2[k] = new_board[k][j]
        result = max(result, get_cnt(sero1))
        result = max(result, get_cnt(sero2))
        new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]

print(result)
