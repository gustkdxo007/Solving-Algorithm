import sys
sys.stdin = open('../INPUT/15656.txt', 'r')

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def get_sequence(k):
    if k == M:
        print(*pick)
        return
    for i in range(N):
        pick.append(arr[i])
        get_sequence(k+1)
        pick.pop()

pick = []
get_sequence(0)