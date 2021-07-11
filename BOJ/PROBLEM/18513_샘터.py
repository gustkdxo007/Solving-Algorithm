import sys
sys.stdin = open('../INPUT/18513.txt', 'r')

from collections import deque

N, K = map(int, input().split())
samtur = list(map(int, input().split()))
Q = deque()
S = set()
for s in samtur:
    Q.append((s, 0))
    S.add(s)
answer = 0
cnt = 0
while Q:
    now, dist = Q.popleft()
    left = now - 1
    right = now + 1
    if  left not in S:
        Q.append((left, dist + 1))
        S.add(left)
        answer += (dist + 1)
        cnt += 1
    if cnt == K:
        break
    if right not in S:
        Q.append((right, dist + 1))
        S.add(right)
        answer += (dist + 1)
        cnt += 1
    if cnt == K:
        break
print(answer)