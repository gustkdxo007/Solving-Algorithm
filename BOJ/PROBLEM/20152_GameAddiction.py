import sys
sys.stdin = open("../INPUT/20152.txt", "r")

H, P = map(int, input().split())
N = max(H, P) + 1
maps = [[0] * N for _ in range(N)]
if H > P:
    H, P = P, H
if H == P:
    print(1)
else:
    maps[H][H] = 0
    for i in range(H, P+1):
        maps[i][H] = 1
    for i in range(H+1, P+1):
        for j in range(H+1, P+1):
            if j > i: continue
            maps[i][j] = maps[i-1][j] + maps[i][j-1]
    print(maps[P][P])

