def solution(n, s):
    if s < n:
        return [-1]
    answer = [s//n] * n
    idx = len(answer) - 1
    for _ in range(s%n):
        answer[idx] += 1
        idx -= 1
    return answer


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))