import sys
sys.stdin = open("../INPUT/2115.txt", "r")

import itertools

def select_beehive(beehives, c):
    max_honey = 0
    for i in range(len(beehives), 0, -1):
        selected_honey = list(itertools.combinations(beehives, i))
        for sh in selected_honey:
            if sum(sh) > c: continue
            honey = 0
            for h in sh:
                honey += (h * h)
            max_honey = max(max_honey, honey)
    return max_honey

T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    beehives = [[*map(int, input().split())] for _ in range(N)]
    result = 0
    for i1 in range(N):
        for j1 in range(N-M+1):
            first_honey = select_beehive(beehives[i1][j1:j1+M], C)
            for i2 in range(i1, N):
                for j2 in range(N-M+1):
                    if i1 == i2 and j2 < j1+M: continue
                    second_honey = select_beehive(beehives[i2][j2:j2+M], C)

                    if first_honey + second_honey > result:
                        result = first_honey + second_honey

    print('#{} {}'.format(t, result))
