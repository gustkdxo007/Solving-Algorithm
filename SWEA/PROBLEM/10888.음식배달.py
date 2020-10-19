import sys
sys.stdin = open('../INPUT/10888.txt', 'r')

import itertools

T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [[*map(int, input().split())] for _ in range(N)]
    houses = []
    franchise = []
    result = 0xffffff
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                houses.append((i, j))
            elif matrix[i][j] > 1:
                franchise.append((i, j))
    for i in range(1, len(franchise)+1):
        allSelected = itertools.combinations(franchise, i)
        results = []
        for selected in allSelected:
            cost = 0
            for hr, hc in houses:
                dist = 0xffffff
                for j in range(len(selected)):
                    dist = min(dist, abs(hr-selected[j][0]) + abs(hr-selected[j][1]))
                cost += dist
            for r, c in selected:
                cost += matrix[r][c]
            results.append(cost)
        result = min(result, min(results))
    print('#{} {}'.format(t, result))

