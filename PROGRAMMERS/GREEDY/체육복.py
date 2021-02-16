def solution(n, lost, reserve):
    clothes = [1] * (n+2)
    clothes[0] = clothes[-1] = 0
    for l in lost:
        clothes[l] -= 1
    for r in reserve:
        clothes[r] += 1
    for i in range(1, n+1):
        if clothes[i] == 0:
            if clothes[i-1] == 2:
                clothes[i] += 1
                clothes[i-1] -= 1
            elif clothes[i+1] == 2:
                clothes[i] += 1
                clothes[i+1] -= 1
    return len(list(filter(lambda x : x > 0, clothes)))


print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
print(solution(3, [1,2], [2,3]))