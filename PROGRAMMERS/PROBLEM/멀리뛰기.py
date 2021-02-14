def solution(n):
    dp = [0] * n
    dp[0] = 1
    if n < 2:
        return dp[n-1]
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1] % 1234567


print(solution(1))
print(solution(3))