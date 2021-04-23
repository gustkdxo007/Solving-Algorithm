import sys
sys.stdin = open("../INPUT/7453.txt", "r")

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
answer = 0
ab_pair = dict()
for a in A:
    for b in B:
        ab_pair[a+b] = ab_pair.get(a+b, 0) + 1

for c in C:
    for d in D:
        answer += ab_pair.get(-(c+d), 0)

print(answer)
