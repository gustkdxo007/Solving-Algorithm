import sys
sys.stdin = open('../INPUT/2003.txt')

N, M = map(int, input().split())
arr = [*map(int, input().split())]
a, b, s = 0, 0, 0
result = 0
for i in range(N):
    s += arr[i]
    b = i
    if s == M:
        result += 1
    if s > M:
        while s > M:
            s -= arr[a]
            a += 1
            if s == M:
                result += 1

print(result)
