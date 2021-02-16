def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    idx = [N] * N
    for i in range(N):
        for j in range(N):
            if board[i][j] and idx[j] == N:
                idx[j] = i
    for m in moves:
        s = idx[m-1]
        if s < N:
            if not stack or stack[-1] != board[s][m-1]:
                stack.append(board[s][m-1])
            elif stack[-1] == board[s][m-1]:
                answer += 2
                stack.pop()
            board[s][m-1] = 0
            idx[m-1] += 1
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[0,2,4,4,2],[0,5,1,3,1]], [1,5,3,5,1,2,1,4]))