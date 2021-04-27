import sys
sys.stdin = open("../INPUT/1202.txt", "r")

import heapq

N, K = map(int, input().split())
answer = 0
weight_minH = []
bag_minH = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(weight_minH, (M, V))

for _ in range(K):
    C = int(input())
    heapq.heappush(bag_minH, (C))

price_maxH = []
while bag_minH:
    possible_weight = heapq.heappop(bag_minH)
    while weight_minH and weight_minH[0][0] <= possible_weight:
        m, v = heapq.heappop(weight_minH)
        heapq.heappush(price_maxH, -v)
    if price_maxH:
        answer -= heapq.heappop(price_maxH)
print(answer)
