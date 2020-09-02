import sys
sys.stdin = open('../INPUT/15665.txt', 'r')

N, M = map(int, input().split())
arr = sorted([*map(int, input().split())])

def get_sequence(k):
    if k == M:
        print(*pick)
        return
    check = []
    for i in range(N):
        if arr[i] in check: continue
        check.append(arr[i])
        pick.append(arr[i])
        get_sequence(k+1)
        pick.pop()

pick = []
get_sequence(0)