import sys
sys.stdin = open('../INPUT/11286.txt', 'r')

import heapq

N = int(input())
Q = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(Q, (abs(x), x))
    else:
        if Q:
            print(heapq.heappop(Q)[1])
        else:
            print(0)
