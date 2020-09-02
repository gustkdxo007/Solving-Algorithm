import sys
from collections import deque
sys.stdin = open('../INPUT/1238.txt', 'r')

def bfs(start):
    queue = list()
    # 현재 노두, 시작점으로부터 떨어진 거리
    queue.append((start, 0))
    # 가장 먼 거리, 가장 큰 숫자
    max_cnt = 0
    max_num = 0
    visited[start] = 1

    while queue:
        c, cnt = queue.pop(0)
        if cnt > max_cnt:
            max_cnt = cnt
            max_num = c
        elif cnt == max_cnt and c > max_num:
            max_num = c
        for i in range(N):
            if adj[c][i] and not visited[i]:
                queue.append((i, cnt+1))
                visited[i] = 1
    return max_num


T = 10
for t in range(1, T+1):
    length, start = map(int, input().split())
    N = 101
    adj = [[0] * N for _ in range(N)]
    data = [*map(int, input().split())]
    visited = [0] * N
    for i in range(0, length, 2):
        adj[data[i]][data[i+1]] = 1

    result = bfs(start)
    print('#{} {}'.format(t, result))