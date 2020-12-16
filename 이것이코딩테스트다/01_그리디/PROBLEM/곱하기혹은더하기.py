import sys
sys.stdin = open('../INPUT/곱하기혹은더하기.txt', 'r')

T = int(input())
for t in range(T):
    S = input()
    result = 0
    for i in range(len(S)):
        if i == 0:
            result = int(S[i])
            continue
        if result * int(S[i]) == 0 or result * int(S[i]) == result:
            result += int(S[i])
        else:
            result *= int(S[i])
    print(result)