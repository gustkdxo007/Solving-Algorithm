dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def solution(n):
    answer = 0
    board = [[0] * n for _ in range(n)]

    def rec(x):
        nonlocal answer
        if x == n:
            answer += 1
            return
        for i in range(n):
            if board[x][i]: continue
            visited = []
            for d in range(8):
                tx, ty = x + dx[d], i + dy[d]
                while 0 <= tx < n and 0 <= ty < n:
                    if board[tx][ty] == 0:
                        board[tx][ty] = 1
                        visited.append((tx, ty))
                    tx += dx[d]
                    ty += dy[d]
            rec(x + 1)
            for vx, vy in visited:
                board[vx][vy] = 0
    rec(0)

    return answer


print(solution(7))