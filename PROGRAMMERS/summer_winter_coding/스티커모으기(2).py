def solution(sticker):
    N = len(sticker)
    DP = [[0] * N for _ in range(2)]
    if len(sticker) < 3:
        return max(sticker)
    DP[0][0], DP[0][1] = sticker[0], sticker[0]
    DP[1][1], DP[1][2] = sticker[1], sticker[1]
    for i in range(1, N-1):
        DP[0][i] = max(DP[0][i-2] + sticker[i], DP[0][i-1])
    for i in range(2, N):
        DP[1][i] = max(DP[1][i-2] + sticker[i], DP[1][i-1])
    return max(max(DP[0]), max(DP[1]))


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
print(solution([9,7,2]))