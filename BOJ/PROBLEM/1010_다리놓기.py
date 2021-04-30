import sys
sys.stdin = open("../INPUT/1010.txt", "r")

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    answer = 1
    for i in range(N):
        answer *= (M-i)
    for i in range(1, N+1):
        answer //= i
    print(answer)