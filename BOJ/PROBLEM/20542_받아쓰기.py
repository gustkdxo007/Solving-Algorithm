import sys
sys.stdin = open('../INPUT/20542.txt', 'r')

N, M = map(int, input().split())
str1 = input()
str2 = input()

DP = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, M+1):
    DP[0][i] = i
for i in range(1, N+1):
    DP[i][0] = i

for i in range(1, N+1):
    for j in range(1, M+1):
        if str1[i-1] == str2[j-1]:
            DP[i][j] = DP[i-1][j-1]
        elif str1[i-1] == 'i' and str2[j-1] in ['j', 'l']:
            DP[i][j] = DP[i-1][j-1]
        elif str1[i-1] == 'v' and str2[j-1] == 'w':
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = min(DP[i-1][j]+1, DP[i][j-1]+1, DP[i-1][j-1]+1)


print(DP[N][M])