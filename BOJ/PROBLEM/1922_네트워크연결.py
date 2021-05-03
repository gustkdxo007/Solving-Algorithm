import sys
sys.stdin = open("../INPUT/1922.txt", "r")

N = int(input())
M = int(input())
edges = []
parents = [i for i in range(N+1)]
answer = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]

def union_set(a, b):
    a = find_set(a)
    b = find_set(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for c, a, b in edges:
    a = find_set(a)
    b = find_set(b)
    if a != b:
        answer += c
        union_set(a, b)

print(answer)