import sys
sys.stdin = open('../INPUT/떡볶이떡만들기.txt', 'r')

def binary_search(arr, t, s, e):
    if s > e:
        return
    mid = (s + e) // 2
    total = 0
    for i in tteok:
        if i > mid:
            total += (i - mid)
    if total == t:
        return mid
    elif total < t:
        return binary_search(arr, t, s, mid-1)
    else:
        return binary_search(arr, t, mid+1, e)



N, M = map(int, input().split())
tteok = [*map(int, input().split())]
print(binary_search(tteok, M, 0, max(tteok)))