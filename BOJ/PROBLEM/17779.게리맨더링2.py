import sys
sys.stdin = open('../INPUT/17779.txt', 'r')

def set_boundary(x, y, d1, d2):
    section[x][y] = 5
    for d in range(1, d1+1):
        dx, dy = x+d, y-d
        if dx > N or dy <= 0: continue
        section[dx][dy] = 5
    for d in range(d2+1):
        dx, dy = x+d1+d, y-d1+d
        if dx > N or dy <= 0 or dy > N: continue
        section[dx][dy] = 5
    for d in range(1, d2+1):
        dx, dy = x+d, y+d
        if dx > N or dy > N: continue
        section[dx][dy] = 5

    for d in range(d1+1):
        dx, dy = x+d2+d, y+d2-d
        if dx > N or dy > N or dy <= 0: continue
        section[dx][dy] = 5

    for i in range(1, N+1):
        arr_j = []
        for j in range(1, N+1):
            if section[i][j] == 5:
                arr_j.append(j)
        if len(arr_j) > 1:
            for d in range(arr_j[0], arr_j[1]+1):
                section[i][d] = 5

def get_result(x, y, d1, d2):
    ward = [0] * 5
    for r in range(1, N+1):
        for c in range(1, N+1):
            if section[r][c] == 5:
                ward[4] += jh[r-1][c-1]
            elif 1 <= r < x+d1 and 1 <= c <= y:
                ward[0] += jh[r-1][c-1]
                section[r][c] = 1
            elif 1 <= r <= x+d2 and y < c <= N:
                ward[1] += jh[r-1][c-1]
                section[r][c] = 2
            elif x+d1 <= r <= N and 1 <= c < y-d1+d2:
                ward[2] += jh[r-1][c-1]
                section[r][c] = 3
            elif x+d2 < r <= N and y-d1+d2 <= c <= N:
                ward[3] += jh[r-1][c-1]
                section[r][c] = 4
    return max(ward) - min(ward)



N = int(input())
jh = [[*map(int, input().split())] for _ in range(N)]

result = 40000

for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x+d1+d2 > N or y-d1 < 1 or y-d1 >= y or y+d2 <= y or y+d2 > N: continue
                section = [([0] * (N + 1)) for _ in range(N + 1)]
                set_boundary(x, y, d1, d2)
                result = min(result, get_result(x, y, d1, d2))
print(result)