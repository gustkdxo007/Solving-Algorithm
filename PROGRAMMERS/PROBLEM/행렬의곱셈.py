def solution(arr1, arr2):
    N = len(arr1)
    M = len(arr2[0])
    answer = [[0] * M for _ in range(N)]
    for i in range(M):
        for j in range(N):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += arr1[j][k] * arr2[k][i]
            answer[j][i] = tmp
    return answer

# def solution(A, B):
#     return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

print(solution([[1,4],[3,2],[4,1]], [[3,3],[3,3]]))
print(solution([[2,3,2],[4,2,4],[3,1,4]], [[5,4,3],[2,4,1],[3,1,1]]))
