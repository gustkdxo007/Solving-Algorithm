import sys
sys.stdin = open("../INPUT/11279.txt", "r")

import heapq

N = int(input())
Q = []
for _ in range(N):
    n = int(input())
    if n > 0:
        heapq.heappush(Q, -n)
    else:
        if len(Q):
            print(-heapq.heappop(Q))
        else:
            print(0)