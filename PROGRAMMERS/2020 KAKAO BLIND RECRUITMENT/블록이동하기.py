from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_next(pos, board):
    new_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상,하,좌,우 움직임
    for d in range(4):
        pos1_dx, pos1_dy, pos2_dx, pos2_dy = pos1_x+dx[d], pos1_y+dy[d], pos2_x+dx[d], pos2_y+dy[d]
        if board[pos1_dx][pos1_dy] or board[pos2_dx][pos2_dy]: continue
        new_pos.append({(pos1_dx, pos1_dy), (pos2_dx, pos2_dy)})
    # 가로로 있을 때
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y] or board[pos2_x+i][pos2_y]: continue
            new_pos.append({(pos1_x+i, pos1_y), (pos1_x, pos1_y)})
            new_pos.append({(pos2_x+i, pos2_y), (pos2_x, pos2_y)})
    # 세로로 있을 때
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i] or board[pos2_x][pos2_y+i]: continue
            new_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
            new_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    return new_pos

def solution(board):
    N = len(board)
    new_board = [[1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]
    visited = []
    Q = deque()
    Q.append(({(1,1),(1,2)}, 0))
    visited.append({(1,1),(1,2)})
    while Q:
        pos, cnt = Q.popleft()
        if (N, N) in pos:
            return cnt
        for np in get_next(pos, new_board):
            if np in visited: continue
            Q.append((np, cnt+1))
            visited.append(np)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))