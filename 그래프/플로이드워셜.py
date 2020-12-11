import sys
sys.stdin = open('플로이드워셜.txt', 'r')

N = int(input())
M = int(input())
INF = int(1e9)
G = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    G[i][i] = 0

for _ in range(M):
    f, t, c = map(int, input().split())
    G[f][t] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            G[i][j] = min(G[i][j], G[i][k]+G[k][j])
for x in G:
    print(x)