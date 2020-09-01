import sys
sys.stdin = open('../INPUT/15657.txt', 'r')

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def get_sequence(s, k):
    if k == M:
        print(*pick)
        return
    for i in range(s, N):
        pick.append(arr[i])
        get_sequence(i, k+1)
        pick.pop()

pick = []
get_sequence(0, 0)