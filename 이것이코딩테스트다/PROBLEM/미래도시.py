import sys
sys.stdin = open('../INPUT/미래도시.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    INF = int(1e9)
    G = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        G[i][i] = 0
    for _ in range(M):
        f, t = map(int, input().split())
        G[f][t] = 1
        G[t][f] = 1
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                G[i][j] = min(G[i][j], G[i][k]+G[j][k])
    X, K = map(int, input().split())
    result = G[1][K] + G[K][X]
    print(result if result < INF else -1)