def make_new_board(m, n, board):
    for i in range(m-1, 1, -1):
        for j in range(n):
            if not board[i][j]:
                tx = i - 1
                while tx >= 0:
                    if board[tx][j]:
                        board[i][j], board[tx][j] = board[tx][j], board[i][j]
                        break
                    tx -= 1
    return board


def find_4block(m, n, board):
    delete = set()
    for i in range(m - 1):
        for j in range(n - 1):
            now = board[i][j]
            if not now: continue
            tmp_del = [(i, j)]
            for d in range(3):
                tx, ty = i + dx[d], j + dy[d]
                if board[tx][ty] != now:
                    tmp_del = []
                    break
                tmp_del.append((tx, ty))
            if tmp_del:
                for tmp in tmp_del:
                    delete.add(tmp)
    for x, y in delete:
        board[x][y] = False
    if delete:
        board = make_new_board(m, n, board)
    return (len(delete), board)


dx = [0, 1, 1]
dy = [1, 1, 0]

def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        cnt, board = find_4block(m, n, board)
        if cnt == 0: break
        answer += cnt

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
