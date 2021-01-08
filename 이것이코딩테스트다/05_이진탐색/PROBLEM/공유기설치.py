import sys
sys.stdin = open('../INPUT/공유기설치.txt', 'r')

N, C = map(int, input().split())
D = [int(input()) for _ in range(N)]
D.sort()
s = D[1] - D[0]
e = D[-1] - D[0]
result = 0

while s <= e:
    mid = (s+e) // 2
    installed = D[0]
    cnt = 1
    for i in range(1, N):
        if D[i] >= installed + mid:
            installed = D[i]
            cnt += 1
    if cnt >= C:
        s = mid + 1
        result = mid
    else:
        e = mid - 1
print(result)