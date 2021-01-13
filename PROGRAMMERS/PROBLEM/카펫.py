def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, int(total ** 0.5)+1):
        if not total % i:
            b = total // i
            if (i-2) * (b-2) == yellow:
                return sorted([i, b], reverse=True)
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))