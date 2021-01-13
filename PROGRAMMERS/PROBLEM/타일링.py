# def solution(n):
#     D = [0] * (n+1)
#     D[1] = 1
#     D[2] = 2
#     for i in range(3, n+1):
#         D[i] = ((D[i-1] + D[i-2]) % 1000000007)
#     return D[n]

def solution(n):
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a+b
    return b


print(solution(4))
print(solution(5))