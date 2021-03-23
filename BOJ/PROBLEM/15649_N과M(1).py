import sys
sys.stdin = open('../INPUT/15649.txt', 'r')

N, M = map(int, input().split())

def get_sequence(idx):
    if idx == M:
        print(*pick)
        return
    for i in range(1, N+1):
        if visited[i]: continue
        visited[i] = 1
        pick.append(i)
        get_sequence(idx+1)
        visited[i] = 0
        pick.pop()

visited = [0] * (N+1)
pick = []
get_sequence(0)