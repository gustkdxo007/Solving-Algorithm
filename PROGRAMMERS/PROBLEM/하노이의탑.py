def solution(n):
    answer = []
    def hanoi(i, from_, to_, assis):
        nonlocal answer
        if i == 1:
            answer.append([from_, to_])
            return
        hanoi(i-1, from_, assis, to_)
        answer.append([from_, to_])
        hanoi(i-1, assis, to_, from_)
    hanoi(n, 1, 3, 2)
    return answer


print(solution(2))