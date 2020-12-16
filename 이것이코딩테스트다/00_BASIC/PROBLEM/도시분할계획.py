import sys
sys.stdin = open('../INPUT/도시분할계획.txt', 'r')

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
for m in range(M):
    f, t, cost = map(int, input().split())
    edges.append((cost, f, t))
edges.sort()
result = 0
last = 0
for cost, f, t in edges:
    if find(f) != find(t):
        union(f, t)
        result += cost
        last = cost
print(result-last)