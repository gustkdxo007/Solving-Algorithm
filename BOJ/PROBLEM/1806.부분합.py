import sys
sys.stdin = open('../INPUT/1806.txt', 'r')

N, S = map(int, input().split())
numbers = [*map(int, input().split())]


sum_ = [0] * (N+1)
for i in range(1, N+1):
    sum_[i] = sum_[i-1] + numbers[i-1]

start = 0
end = 1
cnt = int(1e9)
while start != N:
    if sum_[end] - sum_[start] >= S:
        cnt = min(cnt, end-start)
        start += 1
    else:
        if end == N: break
        end += 1
print(cnt if cnt != int(1e9) else 0)