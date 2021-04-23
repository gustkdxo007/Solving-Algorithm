import sys
sys.stdin = open("../INPUT/2230.txt", "r")

N, M = map(int, input().split())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(n)
arr.sort()
left, right = 0, 1
answer = 2000000001
while right < N:
    tmp = arr[right] - arr[left]
    if tmp == M:
        answer = M
        break
    if tmp < M:
        right += 1
        continue
    answer = min(answer, tmp)
    left += 1
print(answer)
