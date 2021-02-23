def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    n = 0
    for i in range(len(B)):
        if n >= len(A): break
        if A[n] >= B[i]:
            n += 1
            while n < len(A):
                if B[i] > A[n]:
                    n += 1
                    answer += 1
                    break
                n += 1
        else:
            n += 1
            answer += 1
    return answer


# def solution(A, B):
#     answer = 0
#     A.sort()
#     B.sort()
#     j = 0
#
#     for i in range(len(A)):
#         if A[j] < B[i]:
#             answer = answer + 1
#             j = j+1
#
#     return answer


print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))