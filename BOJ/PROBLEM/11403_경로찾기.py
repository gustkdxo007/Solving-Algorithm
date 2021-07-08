import sys
sys.stdin = open('../INPUT/11403.txt', 'r')

N = int(input())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))
routes = [[0] * N for _ in range(N)]

# def find_route(s, now):
#     for i in range(N):
#         if not G[now][i]: continue
#         if routes[s][i]: continue
#         routes[s][i] = 1
#         find_route(s, i)
#
# for i in range(N):
#     find_route(i, i)
# for r in routes:
#     print(*r)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][k] and G[k][j]:
                G[i][j] = 1
for x in G:
    print(*x)