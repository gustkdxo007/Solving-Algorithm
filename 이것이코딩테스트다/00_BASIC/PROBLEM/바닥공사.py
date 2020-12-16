import sys
sys.stdin = open('../INPUT/바닥공사.txt', 'r')

N = int(input())
d = [0] * (N+1)
d[1] = 1
d[2] = 3
for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2] * 2
print(d[N])