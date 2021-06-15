import sys
sys.stdin = open("../INPUT/2224.txt", "r")

N = int(input())
matrix = [[0] * 52 for _ in range(52)]
for _ in range(N):
    f, m, e = input().split()
    if ord(f) <= 90:
        f = ord(f) - 65
    else:
        f = ord(f) - 71
    if ord(e) <= 90:
        e = ord(e) - 65
    else:
        e = ord(e) - 71
    matrix[f][e] = 1
for k in range(52):
    for i in range(52):
        for j in range(52):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

cnt = 0
for i in range(52):
    for j in range(52):
        if i == j: continue
        if matrix[i][j] > 0:
            cnt += 1
print(cnt)

for i in range(52):
    for j in range(52):
        if i == j: continue
        if not matrix[i][j]: continue
        if i < 26:
            f = chr(i+65)
        else:
            f = chr(i+71)
        if j < 26:
            e = chr(j+65)
        else:
            e = chr(j+71)
        print(f, '=>', e)
