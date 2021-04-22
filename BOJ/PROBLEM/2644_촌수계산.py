import sys
sys.stdin = open("../INPUT/2644.txt", "r")

N = int(input())
A, B = map(int, input().split())
M = int(input())
relations = [[] for _ in range(N+1)]
visited = [0] * (N+1)
has_answer = False
def get_degree(n, cnt):
    global has_answer
    visited[n] = 1
    if n == B:
        has_answer = True
        print(cnt)
        return
    for next in relations[n]:
        if visited[next]: continue
        get_degree(next, cnt+1)

for _ in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)
get_degree(A, 0)
if not has_answer:
    print(-1)