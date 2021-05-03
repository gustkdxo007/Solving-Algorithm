import sys
sys.stdin = open("../INPUT/1717.txt", "r")
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
parents = [i for i in range(N+1)]

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

for _ in range(M):
    s, a, b = map(int, input().split())
    if s == 0:
        union_set(a, b)
    elif s == 1:
        a = find_set(a)
        b = find_set(b)
        if a != b:
            print("NO")
        else:
            print("YES")