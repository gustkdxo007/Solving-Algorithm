def solution(a):
    answer = 2
    if len(a) <= 2:
        return len(a)
    l, r = a[0], a[-1]
    S = set()
    for i in range(1, len(a)-1):
        if l > a[i]:
            S.add(a[i])
            l = a[i]
        if r > a[-1-i]:
            S.add(a[-1-i])
            r = a[-1-i]
    return answer + len(S)


print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))