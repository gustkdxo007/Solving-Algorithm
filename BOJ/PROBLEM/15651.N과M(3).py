import sys
sys.stdin = open('../INPUT/15651.txt', 'r')

N, M = map(int, input().split())

def get_sequence(k):
    if k == M:
        print(*pick)
        return
    for i in range(1, N+1):
        pick.append(i)
        get_sequence(k+1)
        pick.pop()

pick = []
get_sequence(0)