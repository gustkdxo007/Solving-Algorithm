def solution(N, stages):
    answer = [0]*(N+2)
    number = len(stages)
    for stage in stages:
        answer[stage] += 1
    for i in range(1, N+1):
        tmp = answer[i]
        if number:
            answer[i] = (tmp / number, i)
            number -= tmp
        else:
            answer[i] = (0, i)
    answer = answer[1:N+1]
    answer.sort(key=lambda x : (-x[0], x[1]))
    return [x[1] for x in answer]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))