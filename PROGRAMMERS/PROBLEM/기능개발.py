import math

def solution(progresses, speeds):
    answer = []
    left_days = [0] * len(progresses)
    for i in range(len(progresses)):
        left_days[i] = math.ceil((100-progresses[i]) / speeds[i])
    tmp = left_days[0]
    cnt = 1
    for i in range(1, len(left_days)):
        if tmp >= left_days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            tmp = left_days[i]
            cnt = 1
        if i == len(left_days)-1:
            answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))