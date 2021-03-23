from collections import deque
from itertools import permutations

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(board, r, c):
    answer = int(1e9)
    N = 4
    card_position = [[] for _ in range(7)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                card_position[board[i][j]].append((i, j))
    cards_n = [x[0] for x in enumerate(card_position) if len(x[1])]
    M = len(cards_n)
    cards_n = [*permutations(cards_n)]

    def bfs(sx, sy, ex, ey):
        visited = [[-1] * N for _ in range(N)]
        Q = deque()
        Q.append((sx, sy))
        visited[sx][sy] = 0
        while Q:
            x, y = Q.popleft()
            for d in range(4):
                tx, ty = x+dx[d], y+dy[d]
                if 0 <= tx < N and 0 <= ty < N and visited[tx][ty] < 0:
                    visited[tx][ty] = visited[x][y] + 1
                    Q.append((tx, ty))
                    if tx == ex and ty == ey:
                        return visited[tx][ty]

                tx, ty = x, y
                while True:
                    tx_, ty_ = tx+dx[d], ty+dy[d]
                    if tx_ < 0 or tx_ >= 4 or ty_ < 0 or ty_ >= 4: break
                    tx, ty = tx_, ty_
                    if board[tx][ty]: break
                if visited[tx][ty] < 0:
                    visited[tx][ty] = visited[x][y] + 1
                    Q.append((tx, ty))
                    if tx == ex and ty == ey:
                        return visited[tx][ty]
        return visited[ex][ey]

    def dfs(x, y, k, s, res):
        nonlocal answer
        if k == M:
            answer = min(answer, res)
            return
        card = cards_n[s][k]
        x1, y1 = card_position[card][0][0], card_position[card][0][1]
        x2, y2 = card_position[card][1][0], card_position[card][1][1]

        cnt1 = bfs(x, y, x1, y1)
        cnt2 = bfs(x1, y1, x2, y2)
        for cx, cy in card_position[card]:
            board[cx][cy] = 0
        dfs(x2, y2, k+1, s, res + cnt1 + cnt2)
        for cx, cy in card_position[card]:
            board[cx][cy] = card

        cnt1 = bfs(x, y, x2, y2)
        cnt2 = bfs(x2, y2, x1, y1)
        for cx, cy in card_position[card]:
            board[cx][cy] = 0
        dfs(x1, y1, k+1, s, res + cnt1 + cnt2)
        for cx, cy in card_position[card]:
            board[cx][cy] = card

    for i in range(len(cards_n)):
        dfs(r, c, 0, i, 0)
    return answer + (M * 2)


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))