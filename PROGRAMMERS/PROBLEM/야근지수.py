def solution(n, works):
    result = 0
    while n > 0:
        works.sort(reverse=True)
        max_ = works and works[0]
        cnt = works.count(max_)
        for i in range(min(cnt, n)):
            if works[i] == 0:
                continue
            works[i] -= 1
        n -= cnt
    for w in works:
        result += w**2
    return result


print(solution(4, [4,3,3]))
print(solution(1, [2,1,2]))
print(solution(3, [1,1]))
