import sys
sys.stdin = open('../INPUT/국영수.txt', 'r')

N = int(input())
S = []
for _ in range(N):
    S.append(input().split())
S.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for s in S:
    print(s[0])