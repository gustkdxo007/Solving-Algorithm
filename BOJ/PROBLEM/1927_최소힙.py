import sys
sys.stdin = open("../INPUT/1927.txt", "r")

import heapq

N = int(input())
Q = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(Q, x)
    else:
        if len(Q) == 0:
            print(0)
        else:
            print(heapq.heappop(Q))
