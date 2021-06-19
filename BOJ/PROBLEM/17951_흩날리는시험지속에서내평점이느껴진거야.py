import sys
sys.stdin = open("../INPUT/17951.txt", "r")

N, K = map(int, input().split())
scores = [*map(int, input().split())]
l = 0
r = 20*N
while l + 1 < r:
    mid = (l+r)//2
    cnt = 0
    tmp_s = 0
    for i in range(N):
        tmp_s += scores[i]
        if tmp_s >= mid:
            cnt += 1
            tmp_s = 0
    if cnt >= K:
        l = mid
    else:
        r = mid
print(l)