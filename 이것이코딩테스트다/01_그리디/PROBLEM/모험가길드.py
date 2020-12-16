import sys
sys.stdin = open('../INPUT/모험가길드.txt', 'r')

N = int(input())
scare = [*map(int, input().split())]
scare.sort()
result = 0
cnt = 0
for i in scare:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0
print(result)