import sys
sys.stdin = open('../INPUT/15666.txt', 'r')

N, M = map(int, input().split())
arr = sorted([*map(int, input().split())])

def get_sequence(s, k):
    if k == M:
        print(*pick)
        return
    check = []
    for i in range(s, N):
        if arr[i] in check: continue
        check.append(arr[i])
        pick.append(arr[i])
        get_sequence(i, k+1)
        pick.pop()

pick = []
get_sequence(0, 0)