import sys
sys.stdin = open('../INPUT/13397.txt', 'r')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = N * 10000

def is_devided_by_M(t):
    _min, _max = arr[0], arr[0]
    cnt = 0
    for i in range(1, N):
        if _min > arr[i]:
            _min = arr[i]
        if _max < arr[i]:
            _max = arr[i]
        if _max - _min > t:
            cnt += 1
            _min, _max = arr[i], arr[i]
    if M > cnt:
        return True
    else:
        return False

left = 0
right = N * 10000
while left <= right:
    mid = (left + right) // 2
    if is_devided_by_M(mid):
        right = mid - 1
        if answer > mid:
            answer = mid
    else:
        left = mid + 1
print(answer)
