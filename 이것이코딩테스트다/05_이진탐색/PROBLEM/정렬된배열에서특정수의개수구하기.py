import sys
sys.stdin = open('../INPUT/정렬된배열에서특정수의개수구하기.txt', 'r')

# def first(arr, t, s, e):
#     if s > e:
#         return
#     mid = (s+e) // 2
#     if (mid == 0 or t > arr[mid-1]) and t == arr[mid]:
#         return mid
#     elif arr[mid] >= t:
#         return first(arr, t, s, mid-1)
#     else:
#         return first(arr, t, mid+1, e)
#
# def last(arr, t, s, e):
#     if s > e:
#         return
#     mid = (s+e) // 2
#     if (mid == len(arr)-1 or t < arr[mid+1]) and t == arr[mid]:
#         return mid
#     elif arr[mid] > t:
#         return last(arr, t, s, mid-1)
#     else:
#         return last(arr, t, mid+1, e)
#
# N = int(input())
# for _ in range(N):
#     n, x = map(int, input().split())
#     numbers = [*map(int, input().split())]
#     a = first(numbers, x, 0, n-1)
#     if not a:
#         print(-1)
#         continue
#     b = last(numbers, x, 0, n-1)
#     print(b-a+1)


import bisect

N = int(input())
for _ in range(N):
    n, x = map(int, input().split())
    numbers = [*map(int, input().split())]
    a = bisect.bisect_left(numbers, x)
    b = bisect.bisect_right(numbers, x)
    print(b-a if b-a else -1)