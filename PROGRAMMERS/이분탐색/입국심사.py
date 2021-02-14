def solution(n, times):
    answer = 0
    times.sort()
    l, r = 0, times[len(times)-1] * n
    while l <= r:
        tmp = 0
        mid = (l + r) // 2
        for time in times:
            tmp += (mid // time)
        if tmp < n:
            l = mid + 1
        else:
            answer = mid
            r = mid - 1
    return answer


print(solution(6, [7, 10]))
print(solution(7, [3, 6, 7]))