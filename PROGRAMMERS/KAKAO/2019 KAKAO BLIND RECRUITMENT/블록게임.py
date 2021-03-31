def solution(board):
    answer = 0
    N = len(board)

    def checkA(x, y, block):
        if y + 1 >= N or y + 2 >= N or x + 1 >= N: return False
        if board[x][y+1] == 0 and board[x][y+2] == 0 and board[x+1][y] == block and board[x+1][y+1] == block and board[x+1][y+2] == block and checkTop2X3(x, y+1, y+2):
            board[x][y], board[x+1][y], board[x+1][y+1], board[x+1][y+2] = 0, 0, 0, 0
            return True
        return False

    def checkB(x, y, block):
        if x + 1 >= N or x + 2 >= N or y - 1 < 0: return False
        if board[x][y-1] == 0 and board[x+1][y-1] == 0 and board[x+2][y-1] == block and board[x+1][y] == block and board[x+2][y] == block and checkTop3X2(x, y-1):
            board[x][y], board[x+1][y], board[x+2][y], board[x+2][y-1] = 0, 0, 0, 0
            return True
        return False

    def checkC(x, y, block):
        if x + 1 >= N or x + 2 >= N or y + 1 >= N: return False
        if board[x][y+1] == 0 and board[x+1][y+1] == 0 and board[x+2][y+1] == block and board[x+1][y] == block and board[x+2][y] == block and checkTop3X2(x, y+1):
            board[x][y], board[x+1][y], board[x+2][y], board[x+2][y+1] = 0, 0, 0, 0
            return True
        return False

    def checkD(x, y, block):
        if y - 1 < 0 or y - 2 < 0 or x + 1 >= N: return False
        if board[x][y-1] == 0 and board[x][y-2] == 0 and board[x+1][y-2] == block and board[x+1][y-1] == block and board[x+1][y] == block and checkTop2X3(x, y-2, y-1):
            board[x][y], board[x+1][y], board[x+1][y-1], board[x+1][y-2] = 0, 0, 0, 0
            return True
        return False

    def checkE(x, y, block):
        if y - 1 < 0 or y + 1 >= N or x + 1 >= N: return False
        if board[x][y-1] == 0 and board[x][y+1] == 0 and board[x+1][y-1] == block and board[x+1][y] == block and board[x+1][y+1] == block and checkTop2X3(x, y-1, y+1):
            board[x][y], board[x+1][y-1], board[x+1][y], board[x+1][y+1] = 0, 0, 0, 0
            return True
        return False

    def checkTop2X3(x, y1, y2):
        while x > 0:
            x -= 1
            if board[x][y1] != 0 or board[x][y2] != 0: return False
        return True

    def checkTop3X2(x, y):
        while x > 0:
            x -= 1
            if board[x][y] != 0: return False
        return True

    while True:
        check_answer = answer
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0: continue
                if checkA(i, j, board[i][j]): answer += 1
                elif checkB(i, j, board[i][j]): answer += 1
                elif checkC(i, j, board[i][j]): answer += 1
                elif checkD(i, j, board[i][j]): answer += 1
                elif checkE(i, j, board[i][j]): answer += 1
        if check_answer == answer: break
    return answer


print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))
print(solution([[0,0,0,0,0,0,0,0,0,0]
,[0,0,0,2,2,0,0,0,0,0]
,[0,0,0,2,1,0,0,0,0,0]
,[0,0,0,2,1,0,0,0,0,0]
,[0,0,0,0,1,1,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0]]))