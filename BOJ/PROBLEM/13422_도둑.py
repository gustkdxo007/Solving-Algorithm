import sys
sys.stdin = open('../INPUT/13422.txt', 'r')

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    money = [0] + list(map(int, input().split()))
    if N == M:
        if sum(money) < K:
            print(1)
        else:
            print(0)
        continue
    money += money[1:M]
    cnt = 0
    for i in range(2, len(money)):
        money[i] += money[i-1]
    for i in range(M, len(money)):
        if money[i] - money[i-M] < K:
            cnt += 1
    print(cnt)