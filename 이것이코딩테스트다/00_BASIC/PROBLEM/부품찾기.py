import sys
sys.stdin = open('../INPUT/부품찾기.txt', 'r')

def binary_search(arr, t, s, e):
    if s > e:
        return 'no'
    mid = (s+e) // 2
    if arr[mid] == t:
        return 'yes'
    elif arr[mid] > t:
        return binary_search(arr, t, s, mid-1)
    else:
        return binary_search(arr, t, mid+1, e)

N = int(input())
item_in_store = [*map(int, input().split())]
M = int(input())
ordered_item = [*map(int, input().split())]
result = []

for i in ordered_item:
    result.append(binary_search(item_in_store, i, 0, N-1))
print(*result)