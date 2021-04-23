import sys
sys.stdin = open("../INPUT/2805.txt", "r")

N, M = map(int, input().split())
trees_height = [*map(int, input().split())]
low, high = 1, 2000000000
while low <= high:
    mid = (low+high) // 2
    tree = 0
    for h in trees_height:
        if h > mid:
            tree += (h-mid)
    if tree < M:
        high = mid - 1
    else:
        low = mid + 1
print(high)