dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# def make_road(x, y, cost, dr, board, visited):
#     global N, answer
#     if cost >= answer:
#         return
#     if x == N-1 and y == N-1:
#         answer = min(answer, cost)
#         return
#     for d in range(4):
#         tx, ty = x+dx[d], y+dy[d]
#         if tx < 0 or tx >= N or ty < 0 or ty >= N or board[tx][ty] or visited[tx][ty]: continue
#         visited[tx][ty] = 1
#         if dr % 2 != d % 2:
#             make_road(tx, ty, cost + 600, d, board, visited)
#         else:
#             make_road(tx, ty, cost + 100, d, board, visited)
#         visited[tx][ty] = 0
#     pass
#
#
# def solution(board):
#     global answer, N
#     answer = int(1e9)
#     N = len(board)
#     visited = [[0] * N for _ in range(N)]
#     visited[0][0] = 1
#     for d in range(2):
#         make_road(0, 0, 0, d, board, visited)
#
#     return answer

from collections import deque

def solution(board):
    N = len(board)
    def get_answer(r, c, dr):
        road = [[int(1e9)] * N for _ in range(N)]
        Q = deque()
        road[r][c] = 0
        Q.append((r, c, 0, dr))
        while Q:
            x, y, cost, direc = Q.popleft()
            for d in range(4):
                tx, ty = x+dx[d], y+dy[d]
                if tx < 0 or tx >= N or ty < 0 or ty >= N or board[tx][ty]: continue
                tmp_cost = cost + 100 if direc % 2 == d % 2 else cost + 600
                if road[tx][ty] > tmp_cost:
                    road[tx][ty] = tmp_cost
                    Q.append((tx, ty, tmp_cost, d))
        return road[-1][-1]
    return min(get_answer(0, 0, 0), get_answer(0, 0, 1))



print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
print(solution([[0,0,1,0,1,1,0,0,0,0], [0,0,0,0,1,0,1,1,0,1], [1,0,0,0,0,1,1,0,1,0], [0,0,0,0,0,0,1,0,0,0], [0,0,0,0,1,0,1,0,1,1],[0,0,1,0,1,1,0,1,0,1],[0,1,0,0,1,0,0,0,1,0],[1,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,1,0,1,0,0], [1,0,0,0,0,0,0,0,1,0]]))