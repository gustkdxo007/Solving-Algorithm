import sys
sys.stdin = open('크루스칼.txt', 'r')

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

edges = []
for i in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge


    if find_parent(a) != find_parent(b):
        union(a, b)
        result += cost
print(result)