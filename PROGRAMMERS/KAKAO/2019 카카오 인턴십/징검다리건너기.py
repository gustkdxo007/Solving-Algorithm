# def solution(stones, k):
#     answer = 0
#     N = len(stones)
#     while True:
#         cnt = 0
#         breaker = False
#         for i in range(N):
#             if stones[i] == 0:
#                 cnt += 1
#                 if cnt == k:
#                     breaker = True
#                     break
#                 continue
#             stones[i] -= 1
#             cnt = 0
#         if breaker: break
#         answer += 1
#     return answer

def is_passed(stones, k, mid):
    cnt = 0
    for stone in stones:
        if stone < mid:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True

def solution(stones, k):
    left = 1
    right = 200000001
    while left < right - 1:
        mid = (left + right) // 2
        if is_passed(stones, k, mid):
            left = mid
        else:
            right = mid
    return left


# print(solution([2,4,5,3,2,1,4,2,5,1], 3))
print(solution([1, 1], 3))