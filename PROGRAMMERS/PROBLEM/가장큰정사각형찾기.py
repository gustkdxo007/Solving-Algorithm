def solution(board):
    R, C = len(board), len(board[0])
    result = 0
    new_board = [[0] * (C+1) for _ in range(R+1)]
    for i in range(0, R):
        for j in range(0, C):
            if board[i][j]:
                new_board[i][j] = min(new_board[i-1][j], new_board[i][j-1], new_board[i-1][j-1]) + 1
                result = max(result, new_board[i][j])
    return result**2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))
print(solution([[1,0],[0,0]]))