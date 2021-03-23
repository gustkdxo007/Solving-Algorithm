import sys
sys.stdin = open('../INPUT/2112.txt', 'r')

import itertools

def check_passed(films, d, w, k):
    for i in range(w):
        cnt = 0
        compared = 0
        is_ok = False
        for j in range(d):
            if compared == films[j][i]:
                cnt += 1
            else:
                cnt = 1
                compared = films[j][i]

            if cnt == k:
                is_ok = True
                break
        if not is_ok:
            return False
    return True

def put_in_drugs(films, n, s, d, w, k, arr):  # k: 최대
    if n == len(arr):
        return check_passed(films, d, w, k)

    for i in range(s, len(arr)):
        tmp = films[arr[i]]
        films[arr[i]] = [0]*w
        if put_in_drugs(films, n+1, i+1, d, w, k, arr):
            return True
        films[arr[i]] = [1]*w
        if put_in_drugs(films, n+1, i+1, d, w, k, arr):
            return True
        films[arr[i]] = tmp
    return False

T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [[*map(int, input().split())] for _ in range(D)]
    result = 0
    breaker = False
    for i in range(K+1):
        selected_position = itertools.combinations([i for i in range(D)], i)
        for arr in selected_position:
            if put_in_drugs(films, 0, 0, D, W, K, arr):
                result = i
                breaker = True
                break
        if breaker:
            break
    print('#{} {}'.format(t, result))
