import sys
sys.stdin = open('../INPUT/15655.txt', 'r')

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def get_sequence(s, k):
    if k == M:
        print(*pick)
        return
    for i in range(s, N):
        if visited[i]: continue
        visited[i] = 1
        pick.append(arr[i])
        get_sequence(i+1, k+1)
        visited[i] = 0
        pick.pop()

visited = [0] * N
pick = []
get_sequence(0, 0)