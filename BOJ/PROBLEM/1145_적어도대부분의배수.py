import sys
sys.stdin = open('../INPUT/1145.txt', 'r')

arr = list(map(int, input().split()))
num = min(arr)

while True:
    cnt = 0
    for n in arr:
        if num % n == 0:
            cnt += 1
    if cnt >= 3:
        break
    num += 1
print(num)
