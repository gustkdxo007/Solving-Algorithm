import sys
sys.stdin = open('../INPUT/15663.txt', 'r')

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def get_sequence(k):
    if k == M:
        print(*pick)
        return
    check = []
    for i in range(N):
        if visited[i]: continue
        if arr[i] in check: continue
        check.append(arr[i])
        visited[i] = 1
        pick.append(arr[i])
        get_sequence(k+1)
        visited[i] = 0
        pick.pop()

visited = [0] * N
pick = []
get_sequence(0)