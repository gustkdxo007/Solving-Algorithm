def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a % 1234567


print(solution(3))
print(solution(5))