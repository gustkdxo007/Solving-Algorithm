import sys
sys.stdin = open('../INPUT/치킨배달.txt', 'r')
from itertools import combinations

N, M = map(int, input().split())
city = [[*map(int, input().split())] for _ in range(N)]
houses = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
candidates = combinations(chicken, M)

def get_distance(candidate):
    total = 0
    for hx, hy in houses:
        distance = int(1e9)
        for cx, cy in candidate:
            distance = min(distance, abs(hx-cx)+abs(hy-cy))
        total += distance
    return total

result = int(1e9)
for candidate in candidates:
    result = min(result, get_distance(candidate))
print(result)