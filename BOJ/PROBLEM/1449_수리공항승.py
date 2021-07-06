import sys
sys.stdin = open('../INPUT/1449.txt', 'r')

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = 0
answer = 0
for p in arr:
    if p < tmp: continue
    tmp = p + L
    answer += 1
print(answer)