def solution(n):
    if n % 2: return 0
    n = n // 2
    answer = [0] * (n+1)
    answer[1] = 3
    for i in range(2, len(answer)):
        answer[i] = (3 * answer[i-1] + sum(answer[:i-1]) * 2 + 2) % 1000000007
    return answer[n]


print(solution(4))