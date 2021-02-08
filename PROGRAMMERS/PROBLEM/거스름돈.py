def solution(n, money):
    matrix = [[0] * (n+1) for _ in range(len(money))]
    for i in range(0, n+1, money[0]):
        matrix[0][i] = 1
    for i in range(1, len(money)):
        for j in range(n+1):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-money[i]]
    return matrix[-1][-1]


print(solution(5, [1,2,5]))