import sys
sys.stdin = open('../INPUT/11055.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
dp = list(arr)
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))