import sys
sys.stdin = open("../INPUT/2331.txt", "r")

A, P = map(int, input().split())
S = []
S.append(A)
def get_result(num):
    num_to_str = str(num)
    next = 0
    for c in num_to_str:
        next += (int(c) ** P)
    if next in S:
        idx = S.index(next)
        return S[:idx]
    else:
        S.append(next)

    return get_result(next)

print(len(get_result(A)))
