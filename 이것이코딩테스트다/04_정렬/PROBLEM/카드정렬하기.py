import sys
sys.stdin = open('../INPUT/카드정렬하기.txt', 'r')

import heapq

N = int(input())
cards = []
for i in range(N):
    heapq.heappush(cards, int(input()))
result = 0
while len(cards) > 1:
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    result += (A+B)
    heapq.heappush(cards, A+B)
print(result)
