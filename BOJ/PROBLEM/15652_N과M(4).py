import sys
sys.stdin = open('../INPUT/15652.txt', 'r')

N, M = map(int, input().split())

def get_sequence(s, k):
    if k == M:
        print(*pick)
        return
    for i in range(s, N+1):
        pick.append(i)
        get_sequence(i, k+1)
        pick.pop()

pick = []
get_sequence(1, 0)