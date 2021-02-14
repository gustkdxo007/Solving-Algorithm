# def solution(m, n, puddles):
#     boards = [[0] * (m+1) for _ in range(n+1)]
#     for x, y in puddles:
#         boards[y][x] = -1
#     boards[1][1] = 1
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if boards[i][j] == -1: continue
#             if boards[i-1][j] + boards[i][j-1] <= -1:
#                 boards[i][j] = -1
#             else:
#                 a = boards[i-1][j] if boards[i-1][j] > 0 else 0
#                 b = boards[i][j-1] if boards[i][j-1] > 0 else 0
#                 boards[i][j] += (a + b) % 1000000007
#     return boards[n][m] if boards[n][m] > 0 else 0

def solution(m, n, puddles):
    boards = [[0] * (m+1) for _ in range(n+1)]
    for x, y in puddles:
        boards[y][x] = -1
    boards[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if boards[i][j] == -1:
                boards[i][j] = 0
                continue
            boards[i][j] += (boards[i-1][j] + boards[i][j-1]) % 1000000007
    return boards[n][m]


print(solution(4, 3, [[2, 4], [3, 2]]))