import sys
sys.stdin = open("../INPUT/1072.txt", "r")

import math

X, Y = map(int, input().split())
rate = math.floor(100 * Y / X)
left, right = 0, 1000000000
answer = 0
if rate >= 99: print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        tx, ty = X+mid, Y+mid
        tmp_rate = math.floor(100 * ty / tx)
        if rate < tmp_rate:
            right = mid - 1
            answer = mid
        elif rate == tmp_rate:
            left = mid + 1
    print(answer)