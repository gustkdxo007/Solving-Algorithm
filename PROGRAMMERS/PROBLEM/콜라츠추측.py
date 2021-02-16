def solution(num):
    answer = 0
    if num == 1:
        return 0
    while answer <= 500:
        answer += 1
        if num % 2:
            num *= 3
            num += 1
        else:
            num //= 2
        if num == 1:
            return answer
    return -1


print(solution(6))
print(solution(16))
print(solution(626331))
print(solution(1))