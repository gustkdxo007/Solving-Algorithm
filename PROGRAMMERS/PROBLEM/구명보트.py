def solution(people, limit):
    answer = 0
    people.sort()
    s, e = 0, len(people) - 1
    while s <= e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        else:
            e -= 1
        answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))