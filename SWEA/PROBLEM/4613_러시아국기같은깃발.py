import sys
sys.stdin = open('../INPUT/4613.txt', 'r')

def select_row(selected, idx, cnt):
    global result
    if cnt == 2:
        # 깃발을 세 부분으로 나눌 수 있음
        a = b = -1
        for i in range(N):
            if selected[i] and a == -1:
                a = i  # 흰색 영역이 끝나는 인덱스
            elif selected[i] and a != -1:
                b = i  # 파란색 영역이 끝나는 인덱스
        cnt = 0
        # 흰색 영역 바꾸는 개수 세기
        for i in range(a+1):
            for j in range(M):
                if flag[i][j] != 'W':
                    cnt += 1
        # 파란색 영역 바꾸는 개수 세기
        for i in range(a+1, b+1):
            for j in range(M):
                if flag[i][j] != 'B':
                    cnt += 1
        # 빨간색 영역 바꾸는 개수 세기
        for i in range(b+1, N):
            for j in range(M):
                if flag[i][j] != 'R':
                    cnt += 1

        if cnt < result:
            result = cnt
        return
    if idx >= N-1:
        return
    selected[idx] = 1
    select_row(selected, idx+1, cnt+1)
    selected[idx] = 0
    select_row(selected, idx+1, cnt)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    result = 2500
#
#     # 흰색 영역. 마지막 2칸은 차지하면 안된다.
#     for i in range(N-2):
#         # 파란색 영역, 마지막 1칸은 차지하면 안된다.
#         for j in range(i+1, N-1):
#             cnt = 0  # 변경이 필요한 갯수
#
#             # 흰색 영역에서 흰색이 아닌 칸 갯수
#             for w in range(i+1):
#                 for k in range(M):
#                     if flag[w][k] != 'W':
#                         cnt += 1
#
#             # 파란 영역에서 파란색이 아닌 칸 갯수
#             for b in range(i+1, j+1):
#                 for k in range(M):
#                     if flag[b][k] != 'B':
#                         cnt += 1
#
#             # 빨간 영역에서 빨간색이 아닌 칸 갯수
#             for r in range(j+1, N):
#                 for k in range(M):
#                     if flag[r][k] != 'R':
#                         cnt += 1
#
#             if cnt < result:
#                 result = cnt
#
    select_row([0]*N, 0, 0)
    print("#{} {}".format(t, result))