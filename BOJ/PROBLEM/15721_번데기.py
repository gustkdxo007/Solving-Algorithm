import sys
sys.stdin = open('../INPUT/15721.txt', 'r')

A = int(input())
T = int(input())
C = int(input())
n = 4
now = 0

while True:
    if now + n < T:
        now += n
        n += 1
    else:
        break
arr = [0, 1, 0, 1] + [0] * (n-2) + [1] * (n-2)
tmp_c = now
now *= 2
for a in arr:
    if a == C:
        tmp_c += 1
    now += 1
    if tmp_c == T:
        break
print((now-1) % A)
