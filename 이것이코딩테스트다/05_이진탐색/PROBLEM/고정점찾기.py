import sys
sys.stdin = open('../INPUT/고정점찾기.txt', 'r')

def binary_search(s, e):
    if s > e:
        return -1
    mid = (s+e) // 2
    if mid == input_number[mid]:
        return mid
    elif mid > input_number[mid]:
        return binary_search(mid+1, e)
    else:
        return binary_search(s, mid-1)

T= int(input())
for t in range(T):
    N = int(input())
    input_number = [*map(int, input().split())]
    print(binary_search(0, N-1))