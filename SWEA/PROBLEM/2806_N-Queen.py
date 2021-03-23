import sys
sys.stdin = open('../INPUT/2806.txt', 'r')

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def n_queen(r):
    global cnt
    # r: 행의 번호, 각 행에서 퀸이 놓일 수 있는 자리 확인
    # 놓일 수 있다면 그 퀸이 영향을 미치는 모든 칸에 표시하고, 다음행으로 진행
    if r == N:  # 행의 끝까지 진행하면 종료. N개의 퀸을 모두 놓았음
        cnt += 1
        return
    # 행의 모든 칸을 조사해서 유망한 칸이 있다면 진행, 아니면 종료
    for i in range(N):
        if not matrix[r][i]:  # 표시가 되지 않음. 유망하다. (퀸을 놓을 수 있음)
            # 퀸을 놓음
            marking(r, i)
            # 다음 행으로 진행
            n_queen(r+1)
            # 퀸을 뺌
            un_marking(r, i)
    pass

def marking(r, c):  # 퀸을 놓았을 때, 해당 퀸이 영향을 미치는 칸에 표시
    for d in range(8):
        nr, nc = r + dr[d], c + dc[d]
        while True:
            if 0 <= nr < N and 0 <= nc < N:
                matrix[nr][nc] += 1
                nr += dr[d]
                nc += dc[d]
            else:
                break
    pass

def un_marking(r, c):  # 퀸에 의해 영향을 받는 칸 표시 되돌리기
    for d in range(8):
        nr, nc = r + dr[d], c + dc[d]
        while True:
            if 0 <= nr < N and 0 <= nc < N:
                matrix[nr][nc] -= 1
                nr += dr[d]
                nc += dc[d]
            else:
                break
    pass

T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    cnt = 0
    n_queen(0)
    print('#{} {}'.format(t, cnt))