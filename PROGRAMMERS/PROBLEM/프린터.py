import collections
def solution(priorities, location):
    answer = 0
    priorities_deque = collections.deque()
    for i in range(len(priorities)):
        if i == location:
            priorities_deque.append((True, priorities[i]))
        else:
            priorities_deque.append((False, priorities[i]))
    while priorities_deque:
        out = priorities_deque.popleft()
        breaker = False
        for tmp in priorities_deque:
            if out[1] < tmp[1]:
                priorities_deque.append(out)
                breaker = True
                break
        if not breaker:
            answer += 1
            if out[0]:
                break
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))