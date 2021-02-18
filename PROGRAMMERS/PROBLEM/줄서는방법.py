# def solution(n, k):
#     result = []
#     visited = [0] * n
#     pick = []
#     cnt = 0
#     ret = 1
#     s = 1
#     for i in range(1, n):
#         ret *= i
#     while cnt + ret <= k:
#         s += 1
#         cnt += ret
#     pick.append(s)
#     visited[s-1] = 1
#     def get_per(l):
#         nonlocal cnt, result
#         if l == n:
#             cnt += 1
#             if cnt == k:
#                 result = [*pick]
#                 return
#             return
#
#         for i in range(n):
#             if visited[i]: continue
#             if cnt > k:
#                 return
#             visited[i] = 1
#             pick.append(i+1)
#             get_per(l+1)
#             pick.pop()
#             visited[i] = 0
#     get_per(len(pick))
#     return result

def solution(n, k):
    result = []
    pick = [x for x in range(1, n+1)]
    while n:
        gap = 1
        for i in range(1, n):
            gap *= i
        idx = (k-1) // gap
        k = k % gap
        result.append(pick.pop(idx))
        n -= 1
    return result


print(solution(4, 17))