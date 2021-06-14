import sys
sys.stdin = open("../INPUT/1655.txt", "r")

import heapq

N = int(input())
min_Q, max_Q = [], []
for i in range(N):
    n = int(input())
    if i % 2:
        heapq.heappush(min_Q, (n, n))
    else:
        heapq.heappush(max_Q, (-n, n))

    if min_Q and max_Q and max_Q[0][1] > min_Q[0][1]:
        max_out = heapq.heappop(max_Q)
        min_out = heapq.heappop(min_Q)
        heapq.heappush(max_Q, (-min_out[1], min_out[1]))
        heapq.heappush(min_Q, (max_out[1], max_out[1]))
    print(max_Q[0][1])