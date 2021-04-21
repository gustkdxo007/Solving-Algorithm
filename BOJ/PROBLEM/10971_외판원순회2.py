import sys
sys.stdin = open("../INPUT/10971.txt", "r")

def get_cost(s, k, cost, start):
    global answer
    if cost > answer: return
    if k == N:
        if not matrix[s][start]: return
        cost += matrix[s][start]
        answer = min(answer, cost)
        return
    for i in range(N):
        if visited[i] or not matrix[s][i]: continue
        visited[i] = 1
        get_cost(i, k+1, cost+matrix[s][i], start)
        visited[i] = 0

N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]
visited = [0] * N
answer = int(1e9)
for i in range(N):
    visited[i] = 1
    get_cost(i, 1, 0, i)
    visited[i] = 0
print(answer)