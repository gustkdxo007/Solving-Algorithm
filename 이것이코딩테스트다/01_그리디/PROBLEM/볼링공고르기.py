import sys
sys.stdin = open('../INPUT/볼링공고르기.txt', 'r')

import itertools

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    K = [*map(int, input().split())]
    comb = itertools.combinations(K, 2)
    result = 0
    for i, j in comb:
        if i != j:
            result += 1
    print(result)