import sys
sys.stdin = open('../INPUT/팀결성.txt', 'r')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for m in range(M):
    oper, a, b = map(int, input().split())
    if oper:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)