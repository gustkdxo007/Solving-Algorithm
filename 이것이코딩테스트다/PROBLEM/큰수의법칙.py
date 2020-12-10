import sys
sys.stdin = open("../INPUT/큰수의법칙.txt", "r")

N, M, K = map(int, input().split())
data = [*map(int, input().split())]
data.sort()
first, second = data[N-1], data[N-2]
result = 0

while M > 0:
    for k in range(K):
        if M == 0: break
        result += first
        M -= 1
    if M == 0: break
    result += second
    M -= 1

print(result)