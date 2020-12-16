import sys
sys.stdin = open('../INPUT/상하좌우.txt', 'r')

N = int(input())
plans = input().split()
r = c = 1
for plan in plans:
    nr, nc = r, c
    if plan == 'R':
        nc += 1
    if plan == 'L':
        nc -= 1
    if plan == 'U':
        nr -= 1
    if plan == 'D':
        nr += 1
    if nr < 1 or nr > N or nc < 1 or nc > N: continue
    r = nr
    c = nc

print(r, c)