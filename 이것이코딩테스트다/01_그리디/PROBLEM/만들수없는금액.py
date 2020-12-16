import sys
sys.stdin = open('../INPUT/만들수없는금액.txt', 'r')

N = int(input())
data = [*map(int, input().split())]
data.sort()
target = 1
for i in data:
    if target < i: break
    target += i
print(target)