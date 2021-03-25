import sys
sys.stdin = open('../INPUT/16562.txt')

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if cost[x] < cost[y]:
        parent[y] = x
    else:
        parent[x] = y

N, M, K = map(int, input().split())
cost = [0] + [*map(int, input().split())]
parents = [x for x in range(N+1)]
result = "Oh no"
for _ in range(M):
    a, b = map(int, input().split())
    if find(parents, a) != find(parents, b):
        union(parents, a, b)
total_cost = 0
for i in range(1, N+1):
    if parents[i] == i:
        total_cost += cost[i]
if total_cost <= K:
    result = total_cost
print(result)