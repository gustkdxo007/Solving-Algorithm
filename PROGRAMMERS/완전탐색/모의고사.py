def solution(answers):
    answer = []
    N = len(answers)
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0] * 3
    for i in range(N):
        if man1[i % len(man1)] == answers[i]:
            cnt[0] += 1
        if man2[i % len(man2)] == answers[i]:
            cnt[1] += 1
        if man3[i % len(man3)] == answers[i]:
            cnt[2] += 1
    max_ = max(cnt)
    for i in range(3):
        if cnt[i] == max_:
            answer.append(i+1)
    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))