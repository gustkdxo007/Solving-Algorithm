import sys
sys.stdin = open('../INPUT/문자열뒤집기.txt', 'r')

S = input()
result = [0, 0]
now = S[0]
for i in range(1, len(S)):
    if now != S[i]:
        result[int(now)] += 1
        now = S[i]
result[int(now)] += 1

print(min(result))