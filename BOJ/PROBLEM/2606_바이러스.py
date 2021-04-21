import sys
sys.stdin = open("../INPUT/2606.txt", "r")

def dfs(n):
    global answer
    visited[n] = 1
    answer += 1
    for next in computers[n]:
        if visited[next]: continue
        dfs(next)

N = int(input())
M = int(input())
computers = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())
    computers[u].append(v)
    computers[v].append(u)
visited = [0] * (N+1)
answer = -1
dfs(1)
print(answer)