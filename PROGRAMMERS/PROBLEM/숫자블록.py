import math

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            q = i // j
            if q > 10000000: continue
            if i % j == 0:
                answer.append(q)
                break
        else:
            answer.append(1)
    return answer


print(solution(3, 12))