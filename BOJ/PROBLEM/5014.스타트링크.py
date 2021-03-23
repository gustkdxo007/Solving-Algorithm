import sys
sys.stdin = open('../INPUT/5014.txt')

from collections import deque

F, S, G, U, D = map(int, input().split())
elevator = [int(1e9)] * (F+1)

Q = deque()
Q.append(S)
elevator[S] = 0
result = 'use the stairs'
while Q:
    now = Q.popleft()
    if now + U <= F and elevator[now] + 1 < elevator[now+U]:
        elevator[now+U] = elevator[now] + 1
        Q.append(now+U)
    if 0 < now - D and elevator[now] + 1 < elevator[now-D]:
        elevator[now-D] = elevator[now] + 1
        Q.append(now-D)

print(elevator[G] if elevator[G] != int(1e9) else result)