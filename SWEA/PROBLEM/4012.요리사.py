import sys
sys.stdin = open("../INPUT/4012.txt", "r")

def get_synerge(selected):
    global result
    synergy_a = 0
    synergy_b = 0
    for i in range(len(selected)):
        for j in range(i+1, len(selected)):
            if selected[i] == 0 and selected[j] == 0:
                synergy_a += (synergy[i][j] + synergy[j][i])
            elif selected[i] == 1 and selected[j] == 1:
                synergy_b += (synergy[i][j] + synergy[j][i])
    result = min(result, abs(synergy_a - synergy_b))

def comb(s, k):
    if k == N//2:
        get_synerge(picked)
        return
    for i in range(s, N):
        picked[i] = 1
        comb(i+1, k+1)
        picked[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    synergy = [[*map(int, input().split())] for _ in range(N)]
    result = float("INF")
    picked = [0] * N
    comb(0, 0)
    print("#{} {}".format(t, result))

# def comb(idx, cnt):
#     if cnt == N//2:  # 원하는
#         pass
#     if idx == N:
#         return
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     synergy = [[*map(int, input().split())] for _ in range(N)]
#