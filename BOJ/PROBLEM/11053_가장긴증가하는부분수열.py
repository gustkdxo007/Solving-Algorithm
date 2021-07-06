import sys
sys.stdin = open('../INPUT/11053.txt')

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
print(dp)