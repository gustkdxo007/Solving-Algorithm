import sys
sys.stdin = open("../INPUT/13251.txt", "r")

M = int(input())
stones = [*map(int, input().split())]
K = int(input())
answer = 0
total = sum(stones)
for i in range(M):
    if stones[i] < K: continue
    tmp = 1
    for k in range(K):
        tmp *= ((stones[i] - k) / (total - k))
    answer += tmp
print(answer)