import sys
sys.stdin = open("../INPUT/1987.txt")


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    global answer, alphabet
    answer = max(answer, len(alphabet))
    for d in range(4):
        tx, ty = x+dx[d], y+dy[d]
        if tx < 0 or tx >= R or ty < 0 or ty >= C or board[tx][ty] in alphabet: continue
        alphabet += board[tx][ty]
        dfs(tx, ty)
        alphabet = alphabet[:-1]

R, C = map(int, input().split())
board = [input() for _ in range(R)]
answer = 0
alphabet = board[0][0]
dfs(0, 0)
print(answer)

